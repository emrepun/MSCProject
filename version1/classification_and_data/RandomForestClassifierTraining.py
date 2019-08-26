import numpy as np
import pandas as pd

#run DataGenerator.py first if the file is missing.

#if it crashes:
#run DataGenerator.py for uniform distribution
#run NormalDistributionGenerator.py for gaussian distribution
data = pd.read_csv('myDataNumericRandomized.csv')
#data = pd.read_csv('normalDistributionData.csv')

X = data.drop('destination', axis=1)
y = data['destination']

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=1)

from sklearn.ensemble import RandomForestClassifier

random = RandomForestClassifier(random_state=42, oob_score=True)

model = random

model.fit(Xtrain, ytrain)

#save model.
import pickle
pickle.dump(model, open('randomForestModel.pkl','wb'))


#For testing purposes, writes results.
#document = open("random_forest_results.doc", "a+")
document = open("normal_distribution_random_forest_results.doc", "a+")
document.write("Score: " + str(model.score(Xtest, ytest)) + "\r\n")
document.close()
