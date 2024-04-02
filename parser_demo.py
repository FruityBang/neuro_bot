import re
import requests
from bs4 import BeautifulSoup


link = 'https://lenta.ru/'
headers = {'User-Agent': 'Mozilla/5'}
resp = requests.get(link, headers=headers)
response = requests.get(link).text

soup = BeautifulSoup(response, 'lxml')
block = soup.find_all(class_='card-mini _longgrid')
block0 = block[0]
block1 = block[0].__dict__['attrs']['href']
block2 = block[0].text
text = block2[:-5]
text2 = block2[-5:]
req = resp.request.headers
print(len(block), block0, block1, text, text2, req, sep='\n')
#print(soup)

