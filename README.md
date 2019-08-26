# MSCProject
Travel Destination Recommender Application with two approaches.

# Version-1
RandomForestClassifier and Neural Network approach.

Application developed with Flutter asks for a set of inputs from user to make classification on server side running flask/Python
with a trained model.

# Version-2
Dynamic Recommender System .

First scoring function, asks for a trip option and makes recommendations by calculating cosine similarity between the type and the city description.

Second scoring function also asks for a trip option and then makes recommendation by calculating cosine similarity and also calcualting a final recommendation score by utilizing feedback from different forms.

Also a classifier is trained and implemented on the application to determine if user feedback is positive and negative.

Hotel_Reviews.csv file can be downloaded from <a href="https://www.kaggle.com/jiashenliu/515k-hotel-reviews-data-in-europe"> here </a>
