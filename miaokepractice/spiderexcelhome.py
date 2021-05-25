import re
import pdfkit
import requests

def html_to_pdf(url, filename):
    conf = pdfkit.configuration(wkhtmltopdf='D:/pdfkit/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdfkit.from_url(url, 'D:/pdf/excelhome.net/word/{}.pdf'.format(filename), configuration=conf)

if __name__ == '__main__':
    j = 0
    k = 0
    for i in range(1,3):
        res = requests.get('https://www.excelhome.net/lesson/article/excel/list_95_{}.html'.format(i))
        content = res.content.decode('gbk')

        # result = re.findall(r'''<a href="(/lesson/article/word/\d+?.html)" class="title" target="_blank">(.+?)</a>''', content)
        result = re.findall(r'''<a href="(/lesson/article/excel/\d+?.html)" class="title" target="_blank">(.+?)</a>''', content)
        for res in result:
            url = 'https://www.excelhome.net'+res[0]
            filename = res[1]
            try:
                print(url, filename)
            except Exception as e:
                j += 1
            k += 1
    print(k,j)
