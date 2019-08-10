import numpy as np
import pandas as pd
import re, math
from collections import Counter

df = pd.read_csv('richCityData.csv')

class DataExaminor:
    def __init__(self):
        print("examinor initialized")

    @staticmethod
    def top_25_words():
        merged_string = ''

        for index, row in df.iterrows():
            merged_string += row['description']

        merged_words = re.compile(r"[\w']+").findall(merged_string)

        counted_words = Counter(merged_words)

        removal_list = []

        #Words manually examined and top 25 words are identified as non contextual.
        for i in counted_words.most_common(25):
            removal_list.append(i[0])

        return removal_list
