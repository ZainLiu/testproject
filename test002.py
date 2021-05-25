# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 15:35:04 2021

@author: Administrator
"""
import requests
from bs4 import BeautifulSoup
# soup=BeautifulSoup(open(r'C:\Users\Administrator\Desktop\practice.html',encoding='utf-8',features='html.parser')  #features值可为lxml


from lxml import etree

# f = open("C:\Users\Administrator\Desktop\practice.html","r",encoding="utf-8") #读取文件
# f = f.read()　　#把文件内容转化为字符串
# html = etree.HTML(f) #把字符串转化为可处理的格式

headers = {

    'authority': 'www.office26.com',
    'method': 'GET',
    'path': '/excel/excel_21491.html',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'Hm_lvt_1409cd7578e9902f74868a83cd7dc2f5=1610005155; Hm_lpvt_1409cd7578e9902f74868a83cd7dc2f5=1610005155',
    'if-modified-since': 'Sun, 20 Dec 2020 13:57:28 GMT',
    'if-none-match': 'W/"5fdf5848-8787"',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

url = 'https://www.office26.com/excel/excel_21491.html'
# req = requests.get(url,headers=headers).content.decode("utf-8")
response = requests.get(url).content.decode("utf-8")
# data = brotli.decompress(response.content)
soup = BeautifulSoup(response, "html.parser")

div = soup.find('div', class_='art-main')

link_list = []
for link in div.find_all('p'):
    print(link)
    if '.png' not in str(link):
        pass
    else:
        pass

    link_list.append(link)
