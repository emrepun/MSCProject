import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={'keywords':'history historical art architecture city culture'})
print(r.json())
