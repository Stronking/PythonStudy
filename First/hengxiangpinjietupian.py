import os
from PIL import Image
import threading

def ZongXiangPingJiePNG(path,width,name,n):
    print(n,"线程正在处理。。。。。")
    UNIT_SIZE = 256  # 图像的宽和高
    height = huoquwenjiangeshu(path)   #文件个数，求图像高度
    TARGET_WIDTH = width * UNIT_SIZE  # 一行有width个图像，那么是width*256那么宽
    png =  'I:\纵向\\' + name + '.png'
    pngfile = open(png,'wb')
    pngfile.write(b"")
    pngfile.close()

    imagefile = []
    for root, dirs, files in os.walk(path):
        for f in files:
            imagefile.append(Image.open(path + '/' + f))
    target = Image.new('RGB', (TARGET_WIDTH, UNIT_SIZE * height))  # 最终拼接的图像的大小为(229*3) * (229*6)
    left = 0
    right = UNIT_SIZE
    jindu = 0
    for image in imagefile:
        target.paste(image, (0, left, TARGET_WIDTH, right))
        left += UNIT_SIZE  # 从上往下拼接，左上角的纵坐标递增
        right += UNIT_SIZE # 左下角的纵坐标也递增　
        quality_value = 100
        jindu+=1
        print(n,"线程当前进度数：",jindu,"   ",image)
        target.save(png, quality=quality_value)
    print(n,"线程处理完成。。")
# path = r"I:\134401-134415"
def huoquwenjiangeshu(path):#路径下文件个数
    l = os.listdir(path)
    m = len(l)
    # print(m)
    return m
# print(huoqulujing(path))
class MyThread(threading.Thread):
    def __init__(self,target,path,width,name,n):
        super(MyThread, self).__init__()
        self.target=target
        self.path=path
        self.width=width
        self.name=name
        self.n =n
    def run(self):
        self.target(self.path,self.width,self.name,self.n)
def thisa():
    #p0 = r"I:\134401-134415"  #完成
    # p1=r"I:\134416-134511"  #没完成
    # p2=r"I:\134512-134527"  #完成
    # p3=r"I:\134528-134543"  #完成
    # p4=r"I:\134544-134559"  #完成
    # p5 = r"I:\134560-134607" #完成
    # p6 = r"I:\134608-134620"  #完成
    p7=r"I:\134416-134431"
    p8=r"I:\134432-134447"
    p9=r"I:\134448-134463"
    p10=r"I:\134464-134479"
    p11=r"I:\134480-134495"
    p12=r"I:\134496-134511"
    p13=r"I:\123"

    # mh1 = MyThread(ZongXiangPingJiePNG,p3,261,"134528-134543",3)
    # mh2 = MyThread(main, p2, 2)
    # mh3 = MyThread(main, p3, 3)
    # mh4 = MyThread(ZongXiangPingJiePNG,p4,255,"134544-134559",4)
    # mh5 = MyThread(ZongXiangPingJiePNG, p5, 261, "134560-134607", 5)
    # mh6 = MyThread(ZongXiangPingJiePNG, p6, 224, "134608-134620", 6)
    mh7 = MyThread(ZongXiangPingJiePNG, p7, 261, "134416-134431", 7)
    mh8 = MyThread(ZongXiangPingJiePNG, p8, 261, "134432-134447", 8)
    mh9 = MyThread(ZongXiangPingJiePNG, p9, 261, "134448-134463", 9)
    mh10 = MyThread(ZongXiangPingJiePNG, p10, 261, "134464-134479", 10)
    mh11 = MyThread(ZongXiangPingJiePNG, p11, 261, "134480-134495", 11)
    mh12 = MyThread(ZongXiangPingJiePNG, p12, 261, "134496-134511", 12)
    mh13 = MyThread(ZongXiangPingJiePNG, p13, 261, "134416-134511", 13)

    # mh1.start()
    # mh2.start()
    # mh3.start()
    # mh4.start()
    # mh5.start()
    # mh6.start()
    # mh7.start()
    # mh8.start()
    # mh9.start()
    # mh10.start()
    # mh11.start()
    # mh12.start()
    mh13.start()

thisa()