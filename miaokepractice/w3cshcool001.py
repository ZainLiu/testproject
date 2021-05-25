import re
import requests


if __name__ == '__main__':
    j = 0
    k = 0
    for i in range(1, 2):
        res = requests.get('https://www.w3cschool.cn/excelvba/list?page={}'.format(i))
        content = res.content.decode('utf8')
        # result = re.findall(r'''<a href="(http://www.officezhushou.com/excelhansu/\d+?.html)">(.+?)</a>''', content)
        result = re.findall(r'''<a href="//(www.w3cschool.cn/excelvba/excelvba-.+?.html)" title="(.+?)">''', content)
        for res in result:
            url = res[0]
            filename = res[1]
            try:
                print(url, filename)

            except Exception as e:
                j += 1
            k += 1
    print(k, j)