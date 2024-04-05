import asyncio
import requests
from bs4 import BeautifulSoup
from trans import make_tatar_wisdom


news_link = 'https://lenta.ru'
joke_url = 'https://www.anekdot.ru/random/anekdot/'
head = {'User-Agent': 'Mozilla/5'}


async def get_rubric_news(url=news_link, suff='', headers=head):
    response = requests.get(url=url+'/rubrics/'+suff, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    news_list = []
    main_block = soup.find(class_='card-feature')
    main_time = main_block.find(class_='card-feature__date').text
    main_title = main_block.text[:-len(main_time)]
    main_new = [main_time, main_title, main_block.__dict__['attrs']['href']]
    news_list.append(main_new)
    blocks = soup.find_all(class_='card-mini _longgrid')
    for block in blocks[:10]:
        block_new = []
        text = block.text
        time = text[-5:]
        title = text[:-5]
        block_new.append(time)
        block_new.append(title)
        block_new.append(block.__dict__['attrs']['href'])
        news_list.append(block_new)
    return news_list


async def get_new(url=news_link, suff='', headers=head):
    response = requests.get(url=url+suff, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    raw_new = soup.find('div', class_='topic-page__container')
    img = raw_new.find('img', class_='picture__image').attrs['src']
    title = raw_new.find('span', class_='topic-body__title').text
    time = raw_new.find(class_='topic-header__item topic-header__time').text
    text_blocks = raw_new.find_all(class_='topic-body__content-text')

    body = ''
    for block in text_blocks:
        block = block.text
        body += block + '\n'

    full_new = '\n'.join([title, body, time])

    return img, full_new


async def get_po_zaslugam(url=joke_url, headers=head):
    response = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    nullable_wisdom = soup.find('div', class_='text').text

    pure_wisdom = await make_tatar_wisdom(nullable_wisdom)
    return pure_wisdom


if __name__ == '__main__':
    print('')
#    print(get_rubric_news(suff=rubrics_dict['Россия']))
#    print(asyncio.run(get_po_zaslugam()))
#    print(asyncio.run(get_new()))
