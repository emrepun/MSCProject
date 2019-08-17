from flask import Flask, request, abort
from cosine_similarity import CosineSimilarity
from rating_extractor import RatingExtractor
from recommender_engine import RecommenderEngine
import operator
import json

app = Flask(__name__)

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

    #recommendations = RecommenderEngine.get_recommendations(keywords)
    recommendations = RecommenderEngine.get_rating_recommendations(keywords)

    return recommendations

if __name__ == '__main__':
    app.run(port=5000, debug=True)
