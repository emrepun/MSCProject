import requests
url = 'http://localhost:5000/api'
#r = requests.post(url,json={'keywords':'history historical art architecture city culture'})
#r = requests.post(url,json={'keywords':'beach beaches park nature holiday sea seaside sand sunshine sun sunny'})
r = requests.post(url,json={'keywords':'nightclub nightclubs nightlife bar bars pub pubs party beer'})
print(r.json())
