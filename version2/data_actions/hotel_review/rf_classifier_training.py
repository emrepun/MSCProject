import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle
import json

#if it crashes, you need to go to root folder of "version2"
#then cd data_actions/hotel_review and run "python3 hotel_review_pre_preocessor.py"
#after that copy reviews.csv to version2/server/
dataset = pd.read_csv('reviews.csv')

sample = 'It was a great experience we were so happy.'

def clean_review(review):
    review = review.lower()
    review = review.split()

    ps = PorterStemmer()

    review = [ps.stem(word) for word in review
                if not word in set(stopwords.words('english'))]

    review = ' '.join(review)

    return review

refactored_reviews = []
limit = len(dataset.index)

for i in range(0, limit):

    review = dataset['review'][i]
    cleared_review = clean_review(review)

    refactored_reviews.append(cleared_review)

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

words = cv.vocabulary_
words_for_json = {}
length = len(words)

for k, v in words.items():
    words_for_json[k] = int(v)


print('Score: ', model.score(X_test, y_test))

pickle.dump(model, open('reviewClassifier.pkl','wb'))
with open('word_feature_space.json', 'w') as fp:
    json.dump(words_for_json, fp)


#print(words)

#sample = 'We are happy to stay in this hotel it was great'
#sample = 'This was unpleasent and horrible experience hotel was dirt i hate it'
#sample = " Very noisy room close to an extrrnal electricity cell buzzing loud all the time air conditioning with poor control cheap fixtures very small room poor value for the money spent quite a lot "
negatives = [
        " Very noisy room close to an extrrnal electricity cell buzzing loud all the time air conditioning with poor control cheap fixtures very small room poor value for the money spent quite a lot ",
        "1 Bed was faulty seemed to dip in the middle very uncomfortable 2 VERY noisy room so got very little sleep because of 1 and 2 3 Make up mirror faulty 4 Cleaning disturbing me when I m trying to get ready for work 5 Concierge whose response was oh dear i was not impressed",
        "Breakfast was okay Typical European but did start at 6am which was good as we had an early flight out",
        "Pity about the two days of rain",
        "Very expensive parking When we booked a 3 adult room we were squeezed to a 2 people room where the extra bed barely fit the booking details were very misleading Had to complain and argue with the staff to finally get upgraded All and all painful experience",
        " Room is a little too minimalistic for my taste but overall was fine There was kind of a weird smell in my room like the carpet was recently shampooed with something strong ",
        " It was a shame that the bar area was being refurbished at the time of our stay",
        " The staff That is the most important thing in a hotel or at least in a luxury hotel I m still waiting for something I asked them They said they will call me back and I m still waiting",
        " The bed was a little uncomfortable for me but my wife liked it just fine ",
        " The rooms are a little dated However the price is a great value You have lovely staff and great space "
      ]

positives = [
            " The room was very nice The included breakfast was very good ",
            " Great location for the Barbican which is why we made the reservation Not so good for the west end ",
            " Beds were very comfortable good selection of breakfast nice lady on the bar",
            "Although the location is not central it is well connected by trams which makes travel easy The room was spacious and the amenities were 5",
            " Staff very helpful was a strong smell of cigarette in our room on the first day they quickly fixed the situation and put in a different better room Mister Porter restaurant food was delicious better than Gaucho in London The spa is nice and very relaxing after a long day walking around the city The swimming pool is definitely a plus big thank you to Cecilia at the SPA she was very welcoming always checked if we didn t need anything Thank you for your time and help I have been very impressed with the quality of the service client from Amsterdam W hotel one of the best I have seen so far from a W hotel and I did quite a few I will definitely come back ",
            " friendly and helpful personal nice room with terrace excellent size of bed",
            " We especially liked the bar where we would always end our hectic days with a relaxing drink or two The bartender Joanna and waiter David were extremely friendly and accommodating and always greeted us with a smile The cocktails were delicious We always looked forward to ending our evening with them The concierge Nik was always eager to provide help and suggestions when asked I would definitely recommend this facility ",
            " Close to the center Living in a hotel of your dreams like a fairy tail the personnel was extremely polite and helpful",
            " I got the room with the view of Arc de Triumph and it was nice I could also see the Eiffel from my room",
            " The wifi facility was good The theme of the hotel was amazing The honesty bar was nice and good set up The staff was really helpful and nice"
            ]

my_trial_positives = [
                     "We had a great time it was very nice highly recommend",
                     "Everything was perfect superb places to visit and experience",
                     "It was a pleasent experience we enjoyed our stay in London a great city with a lot of activities",
                     "Very vivid city a lot of friendly people and great nightlife",
                     "Great old town and many small shops around the city where you can find interesting beautiful products for very cheap prices",
                     "The weather was great and the beaches were both cheap and beautiful highly recommend",
                     "Amazing architecture and lots of museum Saint Petersburg was is a great choice for cultural trips",
                     "We went there for my friends birthday and had a great time in a variety of bars it was superb",
                     "Even though the places were expensive overall we were satisfied and happy with our trip",
                     "Absolutely amazing will visit this city again for sure"

                     ]

my_trial_negatives = [
                     "We had a bad time it was really awful",
                     "Everything was horrible people were unfriendly and disrespectful",
                     "It was an unpleasent experience we disliked our stay it was rather boring",
                     "Even though there were some beautiful beaches and great activities the prices were expensive and we did not like it overall",
                     "It was a dangerous city with a lot of sketch people we had a very bad experience",
                     "It was bad",
                     "Nothing to do the weather was bad and people were staring at us felt unsafe",
                     "Beaches were trash did not like it at all also very expensive",
                     "It was boring will never come here again",
                     "Food was nice but the city was boring it was below average for us"
                     ]

prediction_samples = []

for sample in my_trial_positives:
    big = [0] * length
    clean_sample = clean_review(sample)
    clean_words = re.sub("[^\w]", " ", clean_sample).split()

    for i in clean_words:
        if i in words:
            index = words[i]
            big[index] += 1

    #print(big)
    prediction_samples.append(big)

prd = model.predict(prediction_samples)
print(prd)

prediction_samples = []

for sample in my_trial_negatives:
    big = [0] * length
    clean_sample = clean_review(sample)
    clean_words = re.sub("[^\w]", " ", clean_sample).split()

    for i in clean_words:
        if i in words:
            index = words[i]
            big[index] += 1

    #print(big)
    prediction_samples.append(big)

prd2 = model.predict(prediction_samples)
print(prd2)
