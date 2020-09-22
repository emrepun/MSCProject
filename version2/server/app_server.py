from flask import Flask, request, abort
from cosine_similarity import CosineSimilarity
from rating_extractor import RatingExtractor
from recommender_engine import RecommenderEngine
from review_handler import ReviewHandler
import operator
import json

app = Flask(__name__)

#handle recommendation request.
@app.route('/api/recommendations',methods=['POST'])
def recommend_places():
    print("recommend_places called")
    data = request.get_json(force=True)

    keywords = ''

    try:
        keywords = data['keywords']
    except:
        code = 400
        msg = 'invalid format'
        return msg, code

    #first function makes recommendation only considering Cosine Similarity, second one includes rating information as well.
    #recommendations = RecommenderEngine.get_recommendations(keywords)
    recommendations = RecommenderEngine.get_rating_recommendations(keywords)

    return recommendations

#handle submitted review request.
@app.route('/api/submit_review',methods=['POST'])
def review_received():
    data = request.get_json(force=True)
    review = ''
    try:
        review = data['review']
    except:
        code = 400
        msg = 'invalid review'
        return msg, code

    handler = ReviewHandler()
    return handler.return_review_outcome(review)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
