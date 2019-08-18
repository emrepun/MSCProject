import numpy as np
import pandas as pd
import json
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

class ReviewHandler:

    words = {}

    model = pickle.load(open('reviewClassifier.pkl','rb'))

    def __init__(self):
        print("review handler initialized")
        with open('word_feature_space.json', 'r') as fp:
            self.words = json.load(fp)
            print(len(self.words))
        print('low')

    def clean_review(self, review):
        review = review.lower()
        review = review.split()

        ps = PorterStemmer()

        review = [ps.stem(word) for word in review
                    if not word in set(stopwords.words('english'))]

        review = ' '.join(review)

        return review

    def return_review_outcome(self, review):
        length = len(self.words)
        incoming = [0] * length
        clean_sample = self.clean_review(review)
        clean_words = re.sub("[^\w]", " ", clean_sample).split()

        for i in clean_words:
            if i in self.words:
                index = self.words[i]
                incoming[index] += 1

        outcome = self.model.predict([incoming])

        result = {'outcome': int(outcome[0])}

        return json.dumps(result)
