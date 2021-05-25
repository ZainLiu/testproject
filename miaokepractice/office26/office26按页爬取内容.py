import re
import pdfkit
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    index = 0
    for i in range(169, 170):
        res = requests.get('https://www.office26.com/excel/excel_list_{}.html'.format(i))
        content = res.content.decode('utf8')
        result = re.findall(r'''<a href="(https://www.office68.com/excel/.+?.html)" class="title"><b>(.+?)</b></a>''', content)
        soup = BeautifulSoup(content, "html.parser")
        ul = soup.find('ul', class_='loglist')
        for children in ul.children:
            # image = children.find('img')['src']
            if 'title' in str(children):
                link = children.find('a',class_='h2')['href']
                title = children.find('a',class_='h2').text
                introduction = children.find('div',class_='text').find('p').text
                image_url = children.find('img')['src']
                print(image_url,title,link,introduction)
                index += 1
        print(index)