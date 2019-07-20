import numpy as np
import pandas as pd

import tensorflow as tf

tf.enable_eager_execution()

from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

#run DataGenerator.py first if the file is missing.
data = pd.read_csv('myDataNumericRandomized.csv')

X = data.drop('destination', axis=1)
y = data['destination']

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=1)

model = tf.keras.Sequential([
    layers.Flatten(input_shape=(3, )),
    layers.Dense(64, activation='sigmoid'),
    layers.Dense(32, activation='sigmoid'),
    layers.Dense(12, activation='sigmoid')
    #relu is not good.
    #https://stats.stackexchange.com/questions/126238/
    #what-are-the-advantages-of-relu-over-sigmoid-function-in-deep-neural-networks
])


# 10 epochs each
# 500k data -> flatten(3, ), dense.64, dense.32, dense12 = 0,698 accuracy ( on test 0,76)
# 5k data -> flatten(3, ), dense.64, dense.32, dense12 = 0,1904 accuracy
# 50k data -> flatten(3, ), dense.64, dense.32, dense12 = 0,30 accuracy
# 50k data -> flatten(3, ), dense.128, dense.64, dense.32, dense12 = 0,27 accuracy
# 5M data -> flatten(3, ), dense.64, dense.32, dense12 = 0,635 accuracy (overfitted.) (on test 0,81)

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(Xtrain, ytrain, epochs=10)

test_loss, test_acc = model.evaluate(Xtest, ytest)

print('\nTest accuracy:', test_acc)
