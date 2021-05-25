import re
import pdfkit
import requests

def html_to_pdf(url, filename):
    conf = pdfkit.configuration(wkhtmltopdf='D:/pdfkit/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdfkit.from_url(url, 'D:/pdf/officezhushou.com/ppt/{}.pdf'.format(filename), configuration=conf)

if __name__ == '__main__':
    j = 0
    k = 0
    for i in range(1, 2):
        res = requests.get('http://www.officezhushou.com/excelhansu/list-{}.html'.format(i))
        content = res.content.decode('utf8')
        print(content)

        # result = re.findall(r'''<a href="(http://www.officezhushou.com/pptjiaocheng/\d+?.html)">(.+?)</a>''', content)
        result = re.findall(r'''<a href="(http://www.officezhushou.com/excelhansu/\d+?.html)">(.+?)</a>''', content)
        for res in result:
            url = res[0]
            filename = res[1]
            try:
                print(url,filename)
            except Exception as e:
                j += 1
            k += 1
    print(k, j)