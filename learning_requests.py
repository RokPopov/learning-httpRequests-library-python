import requests

response = requests.get("https://imgs.xkcd.com/comics/python.png")

with open("comic.png", "wb") as f:
    f.write(response.content)

