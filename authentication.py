import requests

# get auth response
response = requests.get("http://httpbin.org/basic-auth/rok/testing", auth=("rok", "testing"))

print(response.text)

# delay response - dynamic data
delayed_response = requests.get("http://httpbin.org/delay/6", timeout=3)