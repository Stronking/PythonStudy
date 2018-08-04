from urllib import request

from bs4 import BeautifulSoup

import time
url = "http://sc.chinaz.com/tupian/beijingtupian.html"
mherders ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

def getHtml(src,herder): #发起连接   得到网页
    req = request.Request(src,headers=herder)
    page = request.urlopen(req)
    html = page.read()
    return html.decode('utf-8')

def getUrl(html):#解析网页，获取连接
    soup = BeautifulSoup(html,'html.parser')
    temp = soup.find('div',class_='clearfix psdk imgload').find_all('p')#解析网页获取图片预览div 获取所有p标签
    # span = soup.find('div',class_='fenye').find_all('a')#解析网页获取页数的
    # print(type(temp))
    urlList=[]   #声明空列表，存储url
    print(temp)
    for i in temp:
        # print(i.a['href'])
        urlList.append(i.a['href'])
    # print(urlList)
    return urlList

def getPageNum(html):
    soup = BeautifulSoup(html,'html.parser')
    span = soup.find('div',class_='fenye').find_all('a')
    s=span[-2].get_text()
    print(s)
    urlList=["http://sc.chinaz.com/tupian/beijingtupian.html"]
    for i in range(2,int(s)):
        surl = "http://sc.chinaz.com/tupian/beijingtupian_"+str(i)+".html"
        urlList.append(surl)
        print(surl)

    return urlList


def sstr(href):  #获取文件名称
    str = href[::-1]    #字符串逆序
    i = str.index('/')   #返回第一个下标
    str = str[0:i]    #截取文件名
    str = str[::-1]  #字符串逆序      两个逆序，正序名称。
    return str   #返回字符串

def ssstr(href):
    i=href.rindex('/')
    str = href[i:]
    return str
def getImg(list): #下载图片
    print(list)
    for i in list:
        html = getHtml(i,mherders)    #函数调用
        soup = BeautifulSoup(html,'html.parser')  #创建bs4对象
        list = soup.find('div',class_='imga').find_all('img')#找到页面中类名为imga的div，在div下面寻找img
        href = list[0].attrs['src'] #获取到img字典中src的对应值，
        req = request.Request(href)#想目标发送链接请求
        reqimg = request.urlopen(req)#获取网页
        img = reqimg.read()#读取网页reponse，二进制
        str=ssstr(href)#名称函数
        print("正在从",href,"下载",str)
        time.sleep(1)
        print("暂停一秒。。。。。。。。")
        path='D:\PythonProject\\venv\MziTuImg\\'+str  #定义文件路径和名称
        file = open(path,'wb')   #打开文件
        file.write(img)  #写入文件
        file.close()  #关闭文件



def main():
    list = getPageNum(getHtml(url,mherders))
    for i in list :
        getImg(getUrl(getHtml(i,mherders)))

main()




