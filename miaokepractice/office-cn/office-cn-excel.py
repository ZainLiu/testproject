import requests
from bs4 import BeautifulSoup, NavigableString

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
    response = requests.get(url).content.decode('utf8', 'ignore')
    soup = BeautifulSoup(response, "html.parser")
    # print(soup)
    section = soup.find('section', class_='article-content')
    for children in section.children:
        if '.jpg' in str(children) or '.gif' in str(children) or '.png' in str(children) or '.jpeg' in str(children):
            image_url = children.find_all('img')[0]['src']
            if image_url:
                print(image_url)
                print('++++++++++++++++++++')
        # span = children.find('span')
        elif isinstance(children,NavigableString):
            if str(children) == '\n' or len(str(children))==0:
                continue
            elif not str(children).replace('\n','').strip():
                continue
            else:
                print(str(children).replace('\n','').strip())
                print('++++++++++++++++++++')
        elif str(children) not in ['\r', '\r\n', '\n', ' ', '<br>', '<br\>', '', '\v', '\x0b', '\f', '\x0c', '\x1c', '\x1d', '\x1e', '\x85', '\u2028', '\u2029' ]:
            text = children.text
            if len(text) != 0 and text not in ['\r', '\r\n', '\n', ' ', '<br>', '<br\>', '', '\v', '\x0b', '\f', '\x0c', '\x1c', '\x1d', '\x1e', '\x85', '\u2028', '\u2029' ]:
                print(text)
                print('++++++++++++++++++++')


if __name__ == '__main__':
    crawl('http://www.office-cn.net/excel-vba/1057.html')