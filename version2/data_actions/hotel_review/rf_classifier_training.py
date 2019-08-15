import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

dataset = pd.read_csv('reviews.csv')

refactored_reviews = []
limit = len(dataset.index)

for i in range(0, limit):

    review = dataset['review'][i]
    review = review.lower()
    review = review.split()

    ps = PorterStemmer()

    review = [ps.stem(word) for word in review
                if not word in set(stopwords.words('english'))]

    review = ' '.join(review)

    refactored_reviews.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(refactored_reviews).toarray()
y = dataset["is_positive"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators = 501,
                            criterion = 'entropy')

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print('Score: ', model.score(X_test, y_test))

pickle.dump(model, open('reviewClassifier.pkl','wb'))
