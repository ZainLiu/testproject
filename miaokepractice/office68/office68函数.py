import re
import pdfkit
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    index = 0
    for i in range(1, 2):
        res = requests.get('https://www.office68.com/excel/list_53_{}.html'.format(i))
        content = res.content.decode('gb2312')
        result = re.findall(r'''<a href="(https://www.office68.com/excel/.+?.html)" class="title"><b>(.+?)</b></a>''', content)
        soup = BeautifulSoup(content, "html.parser")
        ul = soup.find('ul', class_='e2')
        for children in ul.children:
            # image = children.find('img')['src']
            link = children.find('a',class_='title')['href']
            title = children.find('a',class_='title').find('b').text
            introduction = children.find('p',class_='intro').text
            print(title,link,introduction)
            index += 1
        print(index)

