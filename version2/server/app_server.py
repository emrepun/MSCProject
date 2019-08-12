import numpy as np
import pandas as pd
from flask import Flask, request, abort
from cosine_similarity import CosineSimilarity
from rating_extractor import RatingExtractor
import operator
import json

app = Flask(__name__)

df = pd.read_csv('richCityData.csv')

def get_recommendation_score(cs, rating):
    val = abs(rating)
    amount = (cs / 100) * val

    if rating > 0:
        return cs + amount
    else:
        return cs - amount

@app.route('/api',methods=['POST'])
def recommend_places():
    data = request.get_json(force=True)

    keywords = ''

    try:
        keywords = data['keywords']
    except:
        code = 400
        msg = 'invalid format'
        return msg, code

    score_dict = {}

    for index, row in df.iterrows():
        score_dict[index] = CosineSimilarity.cosine_similarity_of(row['description'], keywords)

    #sort cities by score and index.
    sorted_scores = sorted(score_dict.items(), key=operator.itemgetter(1), reverse=True)

    counter = 0

    #create an empty results data frame.
    resultDF = pd.DataFrame(columns=('city', 'popularity', 'description', 'image'))

    #get highest scored 5 cities.
    for i in sorted_scores:
        print(i[0], i[1])
        r = 9
        rating = RatingExtractor.get_rating_weight_no_quantity(r, 5)
        print("score with rating affect", get_recommendation_score(i[1], rating))
        resultDF = resultDF.append({'city': df.iloc[i[0]]['city'], 'popularity': df.iloc[i[0]]['popularity'], 'description': df.iloc[i[0]]['description'], 'image': df.iloc[i[0]]['image']}, ignore_index=True)
        counter += 1

        if counter>4:
            break

    #convert DF to json.
    json_result = json.dumps(resultDF.to_dict('records'))

    #print(get_recommendation_score(sorted_scores[0[1]], 8))

    return json_result

if __name__ == '__main__':
    app.run(port=5000, debug=True)
