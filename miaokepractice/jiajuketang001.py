import re
import requests
import bs4

jiajuketang_list = ['senior',]
if __name__ == '__main__':
    j = 0
    k = 0
    for skillname in jiajuketang_list:
        for i in range(1, 2):
            res = requests.get('https://www.jiajuketang.com/excel/{}/page/{}'.format(skillname,i))
            content = res.content.decode('utf8')
            # result = re.findall(r'''<a href="//(www.w3cschool.cn/excelvba/excelvba-.+?.html)" title="(.+?)">''', content)
            result = re.findall(r'''<h5><a href="(https://www.jiajuketang.com/excel/\d+?.html)">(.+?)</a></h5>''', content)
            for res in result:
                url = res[0]
                filename = res[1]
                try:
                    print(url, filename)

                except Exception as e:
                    j += 1
                k += 1
    print(k, j)