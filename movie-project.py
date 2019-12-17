import requests
import json
api_key = '4d2ea40a'
title = 'Gone Girl'
url = 'http://www.omdbapi.com/?t=' + title + '&apikey=' + api_key
response = requests.get(url)
data = response.json()
print(data)
http://www.omdbapi.com/?t=GoneGirl&apikey=4d2ea40a

import requests
from bs4 import BeautifulSoup as BS

url="https://www.imdb.com/search/title/?title_type=feature&genres=comedy&explore=genres&view=simple"
response = requests.get(url)

soup = BS(response.text, 'html.parser')
urls = soup.find_all('div', class_='lister-list')

for result in urls:
    i = (result.find_all('img')[0])

i['data-tconst']

for result in urls:
    img = result.find_all('img')

#for i in img:
