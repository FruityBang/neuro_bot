import requests
from bs4 import BeautifulSoup
from keys import rubrics_dict


link = 'https://lenta.ru/'
head = {'User-Agent': 'Mozilla/5'}


def get_rubric_news(url=link, suff='', headers=head):
    #print(f'suff = {suff}')
    response = requests.get(url=url+'rubrics/'+suff, headers=headers).text
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




if __name__ == '__main__':
    #print(get_rubric_news(suff=rubrics_dict['Россия']))
