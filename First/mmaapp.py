from urllib import request
from urllib import error
import os
import time, random
import socket



def mkdirAndReturnNmae(path, idname):  # 创建保存目录并返回保存路径及名称
    if os.path.isdir(path):
        name = os.path.join(path, str(idname) + ".png")
        return name
    else:
        os.mkdir(path)
        name = os.path.join(path, str(idname) + ".png")
        return name


def savePng(name, data):
    file = open(name, 'wb')
    file.write(data)
    print(name)
    file.close()


def mian1():
    url8 = 'http://27.17.26.115:8399/arcgis/rest/services/OneMapPublic/GZBGHYZT2000/MapServer/tile/8/'
    headers = {"Referer": "http://whonemap.wpl.gov.cn/map.html",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    path = "I:\map"
    xpx = 187350 #121
    ypx = 134615
    socket.setdefaulttimeout(30)
    while True:
        num = 0
        while True:
            try:
                if xpx < 187382:
                    url = url8 + str(ypx) + "/" + str(xpx)
                    print(url)
                    try:
                        req = request.Request(url, headers=headers)
                        html = request.urlopen(req)
                        savePng(mkdirAndReturnNmae(path + "\\" + str(ypx), xpx), html.read())
                        html.close()
                        xpx += 1
                        time.sleep(1)
                        num = 1
                    except ConnectionResetError or socket.timeout as  rese:
                        print(rese)
                        xpx -= 1
                        time.sleep(5)
                        print("等待五秒。。。。")
                        continue

                else:
                    xpx = 187121
                    break
            except error.HTTPError as e:
                print("HttpError 跳过 ", e)
                time.sleep(0.5)
                xpx += 1
                print(xpx)
                # html.close()
                if num == 1:
                    xpx = 187121
                    break
                # continue
        ypx += 1
        if ypx > 134615:
            print("请求结束。。。。。")
            exit(0)

        time.sleep(1)
mian1()

