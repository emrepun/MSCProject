import numpy as np
import pandas as pd

#run DataGenerator.py first if the file is missing.
data = pd.read_csv('myDataNumericRandomized.csv')

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

#print('Score: ', model.score(Xtest, ytest))
document = open("random_forest_results.doc", "a+")
document.write("Score: " + str(model.score(Xtest, ytest)) + "\r\n")
document.close()

#preds = model.predict(Xtest)
#dog = model.predict([24,2200,0])
# print(Xtest.shape)
# print(type(Xtest))
#print(Xtest)
#print(preds.shape)
#print(preds)
# dog = model.predict(Xtest[10:11])
# #big = [['age', 'budge', 'season'], [50, 4767, 1]]
# a = [25, 4767, 1]
# big = pd.DataFrame([a], columns=['age', 'budget', 'season'])
# print(Xtest[10:11])
# dog2 = model.predict(big)
# print(big)
# print(dog)
# print(dog2)
