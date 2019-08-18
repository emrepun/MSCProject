import requests
url_recommendation = 'http://localhost:5000/api/recommendations'
url_review = 'http://localhost:5000/api/submit_review'

#r = requests.post(url_recommendation,json={'keywords':'history historical art architecture city culture'})
#r = requests.post(url,json={'keywords':'beach beaches park nature holiday sea seaside sand sunshine sun sunny'})
#r = requests.post(url,json={'keywords':'nightclub nightclubs nightlife bar bars pub pubs party beer'})

###########

r = requests.post(url_review,json={'review': 'It was a great experience absolutely superb will do it again highly recommend'})
print(r.json())
