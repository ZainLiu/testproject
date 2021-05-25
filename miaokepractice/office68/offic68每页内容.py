import requests
from bs4 import BeautifulSoup
"""
表示符                                描述
1)	\n                               换行
2)	\r                               回车
3)	\r\n                             回车 + 换行
4)	\v 或 '\x0b'                       行制表符
5)	'\f' 或 '\x0c'                       换表单
6)	'\x1c '                            文件分隔符
7)	'\x1d'                             组分隔符
8)	'\x1e '                            记录分隔符
9)	'\x85  '                           下一行 (C1 控制码)
10)	'\u2028  '                         行分隔符
11)'\u2029  '                         段分隔符
"""

def crawl(url):
    """
    爬取单个网页的数据，即一个练习
    """
    # 创建一个新的practice
    response = requests.get(url).content.decode('gb2312')
    soup = BeautifulSoup(response, "html.parser")

    div = soup.find('td')
    for children in div.children:
        if '.jpg' in str(children) or '.gif' in str(children) or '.png' in str(children) or '.jpeg' in str(children):
            image_url = children.find_all('img')[0]['src']
            if image_url:
                print(image_url)
        # span = children.find('span')
        elif str(children) not in ['\r', '\r\n', '\n', ' ', '<br>', '<br\>', '', '\v', '\x0b', '\f', '\x0c', '\x1c', '\x1d', '\x1e', '\x85', '\u2028', '\u2029' ] :
            text = children.text.replace('\n', '')
            if len(text) != 0:
                print(text)
        # if span:
        #     if span == -1:
        #         continue
        #     else:
        #         text = span.text
        #         if text and text not in ['\r', '\r\n', '\n', ' ', '<br>', '<br\>', '', '\v', '\x0b', '\f', '\x0c', '\x1c', '\x1d', '\x1e', '\x85', '\u2028', '\u2029' ]:
        #             print(text)
        # if text and text != '\n' and text != '<br\>' and len(text) != 0 and text.isspace() == False and text != '\r':
        # if str(children).startswith('<strong>'):
        #     text = children.text
        #     print(text.replace('\n',''))
        # elif text and text not in ['\r', '\r\n', '\n', ' ', '<br>', '<br\>', '', '\v', '\x0b', '\f', '\x0c', '\x1c', '\x1d', '\x1e', '\x85', '\u2028', '\u2029' ]:
        #
        #         print(text.replace('\n',''))
        #
        # else:
        #     if '.jpg' in str(children) or '.gif' in str(children) or '.png' in str(children):
        #         img_url = children['src']
        #         if img_url:
        #             print('https://www.excelhome.net'+img_url)


if __name__ == '__main__':
    # crawl('http://www.excelhome.net/lesson/article/excel/1955.html')
    crawl('https://www.office68.com/excel/25906.html')