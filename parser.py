import requests
from bs4 import BeautifulSoup
from keys import rubrics_dict


link = 'https://lenta.ru/'
head = {'User-Agent': 'Mozilla/5'}


def get_rubric_news(url=link, suff='', headers=head):
    response = requests.get(url=url+suff, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    blocks = soup.find_all(class_='card-mini _longgrid')
    news_list = []
    for block in blocks[:15]:
        block_elem = []
        text = block.text
        time = text[-5:]
        title = text[:-5]
        block_elem.append(time)
        block_elem.append(title)
        block_elem.append(block.__dict__['attrs']['href'])
        news_list.append(block_elem)

    return news_list
#    block1 = blocks[0]
#    block1 = block1.__dict__['attrs']['href']
#    block2 = blocks[1]
#    block2 = block2.text
#    print(block1)
#    print(block2)




if __name__ == '__main__':
    get_rubric_news(suff=rubrics_dict['Россия'])

