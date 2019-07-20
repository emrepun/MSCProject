import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('randomForestModel.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json(force=True)

    age = data['age']
    budget = data['budget']
    season = 0

    if data['season'] == 'spring':
        season = 0
    elif data['season'] == 'autumn':
        season = 1
    elif data['season'] == 'winter':
        season = 2
    elif data['season'] == 'summer':
        season = 3

    sample = [age, budget, season]
    sampleData = pd.DataFrame([sample], columns=['age', 'budget', 'season'])
    prediction = model.predict(sampleData)
    output = {'city': int(prediction[0])}
    print(prediction)
    return jsonify(output)
    #return 'se'

    #prediction = model.predict([[np.array(data['exp'])]])
    #output = prediction[0]
    #return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
