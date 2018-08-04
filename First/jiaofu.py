from bs4 import BeautifulSoup
from selenium import webdriver
import os,time
from urllib import request
url="http://www.99lib.net/book/2303/69139.htm"
ref={"Referer":"http://www.99lib.net/book/2303/69139.htm"}
mheaders={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

def getPage(src):
    # driver = webdriver.Firefox()
    # driver.set_window_size(20000,400000)
    # driver.get(src)
    # data = driver.page_source
    # print(data)
    # return data
    # soup = BeautifulSoup(data,'html')
    # div = soup.find_all('div')
    # for i in div:
    #     print(i.get_text())
    req = request.Request(src,headers=mheaders)
    page = request.urlopen(req)
    html = page.read()
    # print(html.decode("utf-8"))
    return html.decode("utf-8")

def getText(html):
    soup = BeautifulSoup(html,'lxml')
    div = soup.find('div',id='content').find_all('div')
    for i in div:
        print(i)
        # print(i.get_text().replace(' ',''))
    # print(type(div))
getText(getPage(url))
# getPage(url)


