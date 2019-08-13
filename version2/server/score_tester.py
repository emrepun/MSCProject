from rating_extractor import RatingExtractor
from recommender_engine import RecommenderEngine

counts_and_T =  [
                (1000, 50),
                (1000, 100),
                (1000, 200),
                (1000, 1000),
                (1000, 10000),
                (100, 1000),
                (1000, 1000),
                (10000, 1000),
                (1000000, 1000)
                ]

cs = 0.12286 #Similarity score of St. Petersburg
rating = 8.5      #random rating.

#rating affected RC no rating count was = 0.13146, Q=10

for (count, T) in counts_and_T:
    r = RatingExtractor.get_rating_weight_with_quantity(rating = rating, c = count, T = T ,q = 10)
    score = RecommenderEngine.calculate_score_from(cs, r)
    print(score)
