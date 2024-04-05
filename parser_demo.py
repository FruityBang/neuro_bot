import re
import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5'}

joke_url = 'https://www.anekdot.ru/random/anekdot/'
response = requests.get(joke_url).text
soup = BeautifulSoup(response, 'lxml')
joke = soup.find('div', class_='text').text


#joke = 'Мужчина? Как клубок: если выпустить из рук - распускается; взять в руки - сматывается! Выход один - крепко держать за кончик.'
#
#trans_url = 'https://translate.google.com/?hl=ru&sl=ru&tl=tt&text='
#
#symb_to_url = {' ': '%20', ',': '%2C','?': '%3F', ':': '%3A', ';': '%3B'}
#
#for symb in symb_to_url:
#    if symb in joke:
#        joke = joke.replace(symb, symb_to_url[symb])
#
#response = requests.get(trans_url+joke).text
#soup = BeautifulSoup(response, 'lxml')

