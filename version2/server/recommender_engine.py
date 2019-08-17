import numpy as np
import pandas as pd
from cosine_similarity import CosineSimilarity
from rating_extractor import RatingExtractor
import operator
import json

class RecommenderEngine:
    def __init__(self):
        print("engine initialized")


    def calculate_score_from(cs, r):
        amount = (cs / 100) * r

        return cs + amount

    def get_recommendations(keywords):
        df = pd.read_csv('richCityData.csv')

        #keywords = "nightclub nightclubs nightlife bar bars pub pubs party beer"

        score_dict = {}

        for index, row in df.iterrows():
            score_dict[index] = CosineSimilarity.cosine_similarity_of(row['description'], keywords)

        #sort cities by score and index.
        sorted_scores = sorted(score_dict.items(), key=operator.itemgetter(1), reverse=True)

        counter = 0

        #create an empty results data frame.
        resultDF = pd.DataFrame(columns=('city', 'popularity', 'description', 'image'))
        #ratings = [8.5, 3.4, 9.5, 2.3, 7.0]
        #get highest scored 5 cities.
        for i in sorted_scores:
            print(i[0], i[1])
            #r = ratings[counter]
            #rating = RatingExtractor.get_rating_weight_no_quantity(r, 10)
            #print("score with rating affect", r ,RecommenderEngine.calculate_score_from(cs = i[1], r = rating))
            resultDF = resultDF.append({'city': df.iloc[i[0]]['city'], 'popularity': df.iloc[i[0]]['popularity'], 'description': df.iloc[i[0]]['description'], 'image': df.iloc[i[0]]['image']}, ignore_index=True)
            counter += 1

            if counter>4:
                break

        #convert DF to json.
        json_result = json.dumps(resultDF.to_dict('records'))
        return json_result

    def get_rating_recommendations(keywords):
        df = pd.read_csv('ratingRichCityData.csv')

        score_dict = {}

        for index, row in df.iterrows():
            cs = CosineSimilarity.cosine_similarity_of(row['description'], keywords)
            rating = row['rating']
            rating_count = row['rating_count']
            positive_review_count = row['positive_review']
            negative_review_count = row['negative_review']

            rat_value = RatingExtractor.get_rating_with_count_and_reviews(rating,rating_count,positive_review_count,negative_review_count)

            score = RecommenderEngine.calculate_score_from(cs,rat_value)

            score_dict[index] = score

        sorted_scores = sorted(score_dict.items(), key=operator.itemgetter(1), reverse=True)

        counter = 0

        resultDF = pd.DataFrame(columns=('city', 'popularity', 'description', 'image'))

        #get highest scored 5 cities.
        for i in sorted_scores:
            print(i[0], i[1])
            resultDF = resultDF.append({'city': df.iloc[i[0]]['city'], 'popularity': df.iloc[i[0]]['popularity'], 'description': df.iloc[i[0]]['description'], 'image': df.iloc[i[0]]['image']}, ignore_index=True)
            counter += 1

            if counter>4:
                break

        #convert DF to json.
        json_result = json.dumps(resultDF.to_dict('records'))
        return json_result
