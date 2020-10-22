import requests

# GET request
payload_get = {"page": 2, "count": 25}
response_get = requests.get("https://httpbin.org/get", params=payload_get)

print(response_get.text)
print(response_get.url)

# POST request
payload_post = {"username": "rok", "password": "testing"}
response_post = requests.post("https://httpbin.org/post", data=payload_post)

response_dictionary = response_post.json()
print(response_dictionary["form"])