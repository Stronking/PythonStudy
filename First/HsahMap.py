from urllib import request
from bs4 import BeautifulSoup
from xlutils.copy import copy
import xlrd
import xlwt
import os
import time
url='https://etherscan.io/token/generic-tokentxns2?contractAddress=0xb53ac311087965d9e085515efbe1380b2ca4de9a&mode=&p='
mheard={"Referer":"https://etherscan.io/token/0xb53ac311087965d9e085515efbe1380b2ca4de9a","User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
filename='D:/1.xls'
def getHtml(url):

    req = request.Request(url,headers=mheard)
    page = request.urlopen(req)
    html = page.read()
    return html.decode('utf-8')
def getMessage(html):

    soup = BeautifulSoup(html,'html.parser')
    All = soup.find('div',id='maindiv').find_all('tr')
    return All


def mess(url):
    list = getMessage(getHtml(url))
    for i in list[1:]:
        s = i.get_text()
        n = s.find('ago')+3
        m = n + 43
        TxHash=s[:66]
        age=s[67:n]
        From = s[n:n+42]
        To = s[m:m+42]
        Quantity = s[-1:]
        print(TxHash,"****",age,"****",From,"****",To,"****",Quantity)
        excl(filename, TxHash, age, From, To, Quantity)


def write_data(sheet,TxHash,Age,From,To,Quantity, row):
    j=0
    sheet.write(row, j, TxHash)
    j+=1
    sheet.write(row, j, Age)
    j += 1
    sheet.write(row, j, From)
    j += 1
    sheet.write(row, j, To)
    j += 1
    sheet.write(row, j, Quantity)


def excl(filename,TxHash,Age,From,To,Quantity):
    if os.path.exists(filename):
        rb = xlrd.open_workbook(filename, formatting_info=True)
        rn = rb.sheets()[0].nrows
        wb = copy(rb)
        sheet = wb.get_sheet(0)
        write_data(sheet,TxHash,Age,From,To,Quantity, rn)
        os.remove(filename)
        wb.save(filename)
    else:
        header = ['TxHash', 'age', 'From', 'To', 'Quaintity']
        book = xlwt.Workbook(encoding='utf-8')
        sheet = book.add_sheet('数据')
        for h in range(len(header)):
            sheet.write(0, h, header[h])
        write_data(sheet,TxHash,Age,From,To,Quantity,1)
        book.save(filename)

if __name__=="__main__":
    for i in range(1,3558):
        time.sleep(3)
        src = url+str(i)
        mess(src)


