import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from cosine_similarity import CosineSimilarity

app = Flask(__name__)

@app.route('/api',methods=['POST'])
def recommend_places():
    return jsonify({'sample': 'data'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
