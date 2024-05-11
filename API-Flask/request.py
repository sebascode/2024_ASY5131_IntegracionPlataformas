import requests

url = "http://localhost:5000/"
post_response = requests.post(url, json={ 'id': '1', "data": "hola mundo" })
print(post_response.status_code)

google_response = requests.get(url)

print(google_response.content)