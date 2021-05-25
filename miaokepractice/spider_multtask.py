import re
import pdfkit
import requests
import multiprocessing


def html_to_pdf(url, filename):
    conf = pdfkit.configuration(wkhtmltopdf='D:/pdfkit/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdfkit.from_url(url, 'D:/pdf/officezhushou.com/excel函数/{}.pdf'.format(filename), configuration=conf)

def thread_task(result):
    print(11111111)
    for res in result:
        url = res[0]
        filename = res[1]
        try:
            html_to_pdf(url, filename)

        except Exception as e:
            pass

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=10)
    for i in range(1,19):
        res = requests.get('http://www.officezhushou.com/excelhansu/list-{}.html'.format(i))
        content = res.content.decode('utf8')

        result = re.findall(r'''<a href="(http://www.officezhushou.com/excelhansu/\d+?.html)">(.+?)</a>''',
                            content)
        pool.apply_async(thread_task, (result,))
    pool.close()
    pool.join()




