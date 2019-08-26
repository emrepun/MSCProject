import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

#if it crashes go to root folder "version1"
#then cd classification_and_data
#run "python3 RandomForestClassifier.py"
#copy randomForestModel.pkl to version1/server/
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

if __name__ == '__main__':
    app.run(port=5000, debug=True)
