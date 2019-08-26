import pandas as pd
import numpy as np

# read data
#download file: https://www.kaggle.com/jiashenliu/515k-hotel-reviews-data-in-europe
reviews_df = pd.read_csv("Hotel_Reviews.csv")

#only get 1 percent of data. because the data is huge
reviews_df = reviews_df.sample(frac = 0.01, replace = False, random_state=42)

df = pd.DataFrame(columns=('review', 'is_positive'))

#replace missing review info with empty strings
reviews_df = reviews_df.replace(['No Negative', 'No Positive'], ['', ''])

#replace empty strings with NaN value (null) and then drop them.
reviews_df = reviews_df.replace(r'^\s*$', np.nan, regex=True)
reviews_df = reviews_df.dropna()

#only get reviews.
reviews_df = reviews_df[["Negative_Review", "Positive_Review"]]

#separate them
negative_reviews_df = reviews_df[["Negative_Review"]]
positive_reviews_df = reviews_df[["Positive_Review"]]

#add all negative and positive reviews with related label 'is_positive' 0 for negative, 1 for positive.
for index, row in negative_reviews_df.iterrows():
    if "nothing" in row["Negative_Review"]:
        pass
    elif "Nothing" in row["Negative_Review"]:
        pass
    else:
        df = df.append({'review': row["Negative_Review"], 'is_positive': 0}, ignore_index=True)

for index, row in positive_reviews_df.iterrows():
    if "nothing" in row["Positive_Review"]:
        pass
    elif "Nothing" in row["Positive_Review"]:
        pass
    else:
        df = df.append({'review': row["Positive_Review"], 'is_positive': 1}, ignore_index=True)

#save the cleaned data as reviews.csv
endResult = df.to_csv('reviews.csv')
