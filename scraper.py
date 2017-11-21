# Fetching the first 10 tweets from Justin Trudeau

import csv
import requests
from bs4 import BeautifulSoup

url = "https://twitter.com/JustinTrudeau"

response = requests.get(url)
html = response.content
htmlParsed = BeautifulSoup(html, 'html5lib')

allP = htmlParsed.findAll("p", {"class": "TweetTextSize"})

with open("tweets.csv", "w") as tweetFile:
    writer = csv.writer(tweetFile)
    i = 0
    for p in allP:
        i += 1
        writer.writerow([i, p.getText()])

