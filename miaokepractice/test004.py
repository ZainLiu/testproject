import requests
from bs4 import BeautifulSoup


def crawl(url):
    """
    爬取单个网页的数据，即一个练习
    """
    # 创建一个新的practice
    content_list = []
    response = requests.get(url).content.decode("utf-8")
    # data = brotli.decompress(response.content)
    soup = BeautifulSoup(response, "html.parser")

    div = soup.find('div', class_='art-main')
    index = 1
    for link in div.children:
        print(link)
        if '.png' in str(link) or '.jpg' in str(link):
            text = link.string
            if text and text not in ['\n', ' ']:
                # 图文piece
                content_list.append(text)
                index += 1
                image_url = link.find_all('img')[0]['src']
                if image_url:
                    content_list.append(image_url)
                    index += 1
            else:
                image_url = link.find_all('img')[0]['src']
                if image_url:
                    content_list.append(image_url)
                    index += 1
        else:
            text = link.string
            if text and text not in ['\n',' ']:
                content_list.append(text)
                index += 1

    print(content_list)

if __name__ == '__main__':
    crawl('https://www.office26.com/excel/excel_21489.html')