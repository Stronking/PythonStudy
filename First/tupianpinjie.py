# import os
# from PIL import Image
#
# path = "I:/map"
#
#
# # listpath = os.listdir(path)
# # pngListPath=[]
# # for i in listpath:
# #     pngListP = os.path.join(path,i)
# #     pngListPath.append(pngListP)
# # print(pngListPath)
# # for i in pngListPath:
# #     pngList = os.listdir(i)
# #     print(pngList[0])
# # pngNumber = len(pngList)
# # print(pngNumber)
# def GetList(path):
#     list = os.listdir(path)
#     return list
#
#
# def addPng(path):
#     p = os.path.join("I:/map", path)
#     print(p)
#     # os.makedirs(p + '/result')
#     png =  'I:/result/' + path + '.png'
#     pngfile = open(png,'wb')
#     pngfile.write(b"")
#     pngfile.close()
#     UNIT_SIZE = 256  # 单个图像的大小为229*229
#     LENG = len(os.listdir(p))
#     print(LENG)
#     TARGET_WIDTH = LENG * UNIT_SIZE  # 拼接完后的横向长度为6*229
#
#     images = []  # 先存储所有的图像的名称
#     for root, dirs, files in os.walk(p):
#         for f in files:
#             images.append(f)
#     print(p)
#     for i in range(len(images) // LENG):  # LENG个图像为一组
#         imagefile = []
#         j = 0
#         for j in range(LENG):
#             imagefile.append(Image.open(p + '/' + images[j]))
#             print("正在增加。。。")
#         target = Image.new('RGB', (TARGET_WIDTH, UNIT_SIZE))
#         left = 0
#         right = UNIT_SIZE
#         for image in imagefile:
#             target.paste(image, (left, 0, right, UNIT_SIZE))  # 将image复制到target的指定位置中
#             left += UNIT_SIZE  # left是左上角的横坐标，依次递增
#             right += UNIT_SIZE  # right是右下的横坐标，依次递增
#             quality_value = 100  # quality来指定生成图片的质量，范围是0～100
#
#
#             target.save(png, quality=quality_value)
#         imagefile = []
#
#
# def main():
#     list = GetList(path)
#     for i in list:
#         print(i)
#         addPng(i)
# main()

import os
from PIL import Image
import threading

# path = "I:/map"


# listpath = os.listdir(path)
# pngListPath=[]
# for i in listpath:
#     pngListP = os.path.join(path,i)
#     pngListPath.append(pngListP)
# print(pngListPath)
# for i in pngListPath:
#     pngList = os.listdir(i)
#     print(pngList[0])
# pngNumber = len(pngList)
# print(pngNumber)
def GetList(path):
    list = os.listdir(path)
    return list


def addPng(path,dir,n):
    p = os.path.join(dir, path)
    print(n,p)
    # os.makedirs(p + '/result')
    png =  'I:/result/' + path + '.png'
    pngfile = open(png,'wb')
    pngfile.write(b"")
    pngfile.close()
    UNIT_SIZE = 256  # 单个图像的大小为229*229
    LENG = len(os.listdir(p))
    print(LENG)
    TARGET_WIDTH = LENG * UNIT_SIZE  # 拼接完后的横向长度为6*229

    images = []  # 先存储所有的图像的名称
    for root, dirs, files in os.walk(p):
        for f in files:
            images.append(f)
    print(p)
    for i in range(len(images) // LENG):  # LENG个图像为一组
        print(n,"线程--------------------------------------------------------------------")
        imagefile = []
        j = 0
        for j in range(LENG):
            imagefile.append(Image.open(p + '/' + images[j]))
            # print(n,"正在增加。。。")
        target = Image.new('RGB', (TARGET_WIDTH, UNIT_SIZE))
        left = 0
        right = UNIT_SIZE
        for image in imagefile:
            target.paste(image, (left, 0, right, UNIT_SIZE))  # 将image复制到target的指定位置中
            left += UNIT_SIZE  # left是左上角的横坐标，依次递增
            right += UNIT_SIZE  # right是右下的横坐标，依次递增
            quality_value = 100  # quality来指定生成图片的质量，范围是0～100


            target.save(png, quality=quality_value)
        imagefile = []


def main(path,n):
    print(n,path)
    list = GetList(path)
    for i in list:
        print(n,"线程处理：",i)
        addPng(i,path,n)
    print(n,"线程结束。。。。")

class MyThread(threading.Thread):
    def __init__(self,target,args,num):
        super(MyThread, self).__init__()
        self.target=target
        self.args=args
        self.num=num
    def run(self):
        self.target(self.args,self.num)
def thisa():
    p1=r"I:\608-620"
    # p2=r"I:\560-607"
    p3=r"I:\544-559"
    # print(p1)
    mh1 = MyThread(main,p1,1)
    # mh2 = MyThread(main, p2, 2)
    mh2 = MyThread(main, p3, 2)
    mh1.start()
    mh2.start()
    # mh3.start()

thisa()

