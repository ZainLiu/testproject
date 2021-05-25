import requests
import re
import pdfkit


def html_to_pdf(url, filename):
    conf = pdfkit.configuration(wkhtmltopdf='D:/pdfkit/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdfkit.from_url(url, 'D:/pdf/excelcn.com/{}.pdf'.format(filename), configuration=conf)

if __name__ == '__main__':
    i = 0
    with open('233.html','r',encoding='utf8') as f:
        res = re.findall(r'<a href="(http://www.excelcn.com.+?.html)" title=".+?" .+?>(.+?)</a>',f.read())
        print(len(res), res)
        for html in res:
            try:
                html_to_pdf(html[0],html[1])
            except Exception as e:
                i+=1
        print(i)
