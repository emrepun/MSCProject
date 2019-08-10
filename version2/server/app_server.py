import numpy as np
import pandas as pd
from flask import Flask, request, abort
from cosine_similarity import CosineSimilarity
import operator
import json

app = Flask(__name__)

df = pd.read_csv('richCityData.csv')

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
        resultDF = resultDF.append({'city': df.iloc[i[0]]['city'], 'popularity': df.iloc[i[0]]['popularity'], 'description': df.iloc[i[0]]['description'], 'image': df.iloc[i[0]]['image']}, ignore_index=True)
        counter += 1

        if counter>4:
            break

    #convert DF to json.
    json_result = json.dumps(resultDF.to_dict('records'))

    return json_result

if __name__ == '__main__':
    app.run(port=5000, debug=True)
