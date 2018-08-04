from urllib import request
from bs4 import BeautifulSoup
import os
import time
import random

src = "myyu?44|||3rnyz3htr4fqq"
mheaders = {'referer': 'http://www.mzitu.com/139731/3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
mmheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
def decode(key):
    m=''
    for i in key:
        n = ord(i) - 5
        t = chr(n)
        m = m + t
    return m
def getHtml(url):  # 获取网页
    req = request.Request(url, headers=mmheaders)
    page = request.urlopen(req)
    html = page.read()
    return html.decode('utf-8')
def getAllUrl(html):  # 解析网页，获取URL与名称

    soup = BeautifulSoup(html, 'html.parser')
    AllUrl = soup.find('ul', class_='archives').find_all('a')
    # AllUrl.AllUrl
    list = {}#设置空字典
    for i in AllUrl:
        a = i.attrs['href']
        b = i.get_text()
        list.setdefault(b, a) #加入到字典中
    return list
def getPageNum(url):  # 获取页数
    html = getHtml(url)
    soup = BeautifulSoup(html, 'html.parser')
    span = soup.find('div', class_='pagenavi').find_all('span')
    num = span[-2].get_text()
    return int(num)
def getImgUrl(url):  # 获取图片地址
    html = getHtml(url)
    soup = BeautifulSoup(html, 'html.parser')
    imgUrl = soup.find('div', class_='main-image').find_all('img')
    Url = imgUrl[0].attrs['src']
    return Url
def mkdirToSaveImg(path, name):  #创建保存目录
    if os.path.isdir(path):#路径判断，是否为文件目录
        dir = os.path.join(path, 'Python1808\\'+name)    #生成目录地址1
        dir2= os.path.join(path,'Python1808\\'+name[0])  #生成目录地址2
        if os.path.exists(dir):#判断目录是否存在
            os.makedirs(dir+str(random.randint(1,100000)))  #创建目录
            return dir + str(random.randint(1, 100000))
        else:
            try : #有异常或者错误，执行except
                os.makedirs(dir)   #创建目录，
                return dir
            except NotADirectoryError:  #目录名称不合法的话，抛出异常，执行下面语句
                print(dir)
                os.makedirs(dir2)
                return dir2

        #print('保存路径是：' + dir)

    else:
        dir = "C:\\Images\\" +'Python1808\\' +name   # 生成目录地址1
        dir2 = "C:\\Images\\" + 'Python1808\\'+name[2]  # 生成目录地址2
        if os.path.exists(dir):  # 判断目录是否存在
            os.makedirs(dir + str(random.randint(1, 100000)))  # 创建目录
            return dir + str(random.randint(1, 100000))
        else:
            try:  # 有异常或者错误，执行except
                os.makedirs(dir)  # 创建目录，
                return dir
            except NotADirectoryError:  # 目录名称不合法的话，抛出异常，执行下面语句
                print(dir)
                os.makedirs(dir2)
                return dir2
def name(href):
    i = href.rindex('/') #从右边往左找/返回下标
    str = href[i:] #截取名称
    return str
def saveImg(url,path):#下载图片函数
    p=path+name(url) #保存路径加文件名称
    file = open(p, 'wb') #打开文件，以二进制形式写入write  Binary
    req = request.Request(url,headers=mheaders) #发送网页请求
    img=request.urlopen(req) #打开链接
    t=img.read() #通过链接读取网页数据
    print("正在下载图片。。。。。",name(url))
    file.write(t) #将数据写入文件
    file.close()#关闭文件缓冲区


def getAllImgUrlAndSaveImg():
    list = getAllUrl(getHtml(decode(src)))   #获取所有网页链接
    path = input("请输入保存路径：")  #键入路径
    for k, v in list.items():   #遍历字典
        dir = mkdirToSaveImg(path, k)   #获取路径
        imgHref = getImgUrl(v) #获取图片第一个链接
        for i in range(1,getPageNum(v)):
            if i < 10:
                s = imgHref[:len(imgHref) - 5] + str(i) + '.jpg' #拼接图片链接
                saveImg(s,dir)  #调用下载图片函数
            else:
                s = imgHref[:len(imgHref) - 6] + str(i) + '.jpg'#拼接图片链接
                saveImg(s, dir)#调用下载图片函数
        time.sleep(2) #防止封IP休眠两秒中








getAllImgUrlAndSaveImg()



