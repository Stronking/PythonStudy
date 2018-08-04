import threading
import time
from urllib import request
from urllib import error
import os
import socket
import selenium



class MyThread(threading.Thread):
    """
        属性:
        target: 传入外部函数, 用户线程调用
        args: 函数参数
        """

    def __init__(self, target, args,krgs):
        super(MyThread, self).__init__()  # 调用父类的构造函数
        self.target = target
        self.args = args
        self.krgs= krgs

    def run(self):
        self.target(self.args,self.krgs)
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
    # print(name)
    file.close()


def mian(ypx,n):
    url8 = 'http://27.17.26.115:8399/arcgis/rest/services/OneMapPublic/GZBGHYZT2000/MapServer/tile/8/'
    headers = {"Referer": "http://whonemap.wpl.gov.cn/map.html",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    path = "I:\map"
    xpx = 187121 #121
    y = ypx+3
    socket.setdefaulttimeout(30)
    while True:
        num = 0
        while True:
            try:
                if xpx < 187382:
                    url = url8 + str(ypx) + "/" + str(xpx)
                    print(n,"线程的下载",url)
                    try:
                        req = request.Request(url, headers=headers)
                        html = request.urlopen(req)
                        savePng(mkdirAndReturnNmae(path + "\\" + str(ypx), xpx), html.read())
                        html.close()
                        xpx += 1
                        time.sleep(1)
                        num = 1
                    except ConnectionResetError  as  rese:
                        print(n,rese)
                        xpx -= 1
                        time.sleep(5)
                        print(n,"————————————————————————————————————————等待五秒。。。。")
                        continue
                    except socket.timeout as  stout:
                        print(n,stout)
                        xpx -= 1
                        time.sleep(5)
                        print(n,"————————————————————————————————————————等待五秒。。。。")
                        continue
                    except TimeoutError as  timeout:
                        print(n, timeout)
                        xpx -= 1
                        time.sleep(5)
                        print(n, "————————————————————————————————————————等待五秒。。。。")
                        continue


                else:
                    xpx = 187121
                    break
            except error.HTTPError as e:
                print(n,"HttpError 跳过 ", e)
                time.sleep(0.5)
                xpx += 1
                print(n , "线程    ",xpx)
                # html.close()
                if num == 1:
                    xpx = 187121
                    break
                # continue
        ypx += 1
        if ypx >= y:
            print(n,"线程  即将结束 ",ypx)
            print(n,".。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。请求结束。。。。。")
            exit(0)

        time.sleep(1)
def main():
    mh1 = MyThread(mian,134599,1)  #574 开始+10
    mh2 = MyThread(mian,134602,2)  #584
    mh1.start()
    mh2.start()
    k=time.time()

main()
