import requests
from bs4 import BeautifulSoup


def crawl_office26_per_page(url):
    """爬取office26每页数据"""
    # practice = Practice.objects.create(
    #     level=level,
    #     name=practice_title,
    #     status=2
    # )
    # section = Section.objects.create(
    #     practice=practice,
    #
    # )
    response = requests.get(url).content.decode("utf-8")
    soup = BeautifulSoup(response, "html.parser")

    div = soup.find('div', class_='art-main')
    index = 1
    for link in div.children:
        # print(link)
        if '.png' in str(link) or '.jpg' in str(link) or '.gif' in str(link):
            text=link.text
            if text and len(text) != 0 and str(text) not in ['\r', '\r\n', '\n', ' ', '<br>', '<br\>', '', '\v', '\x0b', '\f', '\x0c', '\x1c', '\x1d', '\x1e', '\x85', '\u2028', '\u2029','\xc2\xa0']:
                print(text.strip())
            image_url = link.find('img')['src']
            if 'https://www.office26.com' not in image_url:
                image_url = 'https://www.office26.com' + image_url
            print(image_url)
        elif str(link) != '\n' and len(str(link)) != 0:
            text = link.text.replace('\n','').replace('\xa0', '')
            if text and text not in ['\r', '\r\n', '\n', ' ', '<br>', '<br\>', '', '\v', '\x0b', '\f', '\x0c', '\x1c', '\x1d', '\x1e', '\x85', '\u2028', '\u2029','\xc2\xa0' ]:
                print(text.strip())

if __name__ == '__main__':
    crawl_office26_per_page('https://www.office26.com/excel/excel_21489.html')

    """
    https://www.office26.com/excel/excel_21491.html 
    https://www.office26.com/excel/excel_6.html
    """