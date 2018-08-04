import os
from PIL import Image
import threading

path = r"I:\已完成"

listpath = os.listdir(path)
listn = []
for i in listpath:
    p=os.path.join(path,i)
    listn.append(p)
print(len(listn))
for i in listn:
    n = os.listdir(i)
    print(i,"里面文件个数",len(n),"第一个文件名称",n[0],"最后一个文件名称",n[-1])



# def addPng(path,dir,n):
#     p = os.path.join(dir, path)
#     print(n,p)
#     # os.makedirs(p + '/result')
#     png =  'I:/result/' + path + '.png'
#     pngfile = open(png,'wb')
#     pngfile.write(b"")
#     pngfile.close()
#     UNIT_SIZE = 256  # 单个图像的大小为256*256
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
#         print(n, "线程正在增加。。。")
#         for j in range(LENG):
#             imagefile.append(Image.open(p + '/' + images[j]))
#             # print(n,"正在增加。。。")
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
# def main(path,n):
#     print(n,path)
#     list = GetList(path)
#
#     for i in list:
#         print(n, "线程处理：", i)
#         print(i)
#         addPng(i,path,n)
#     print(n, "线程结束。。。。")
#
#
# class MyThread(threading.Thread):
#     def __init__(self,target,args,num):
#         super(MyThread, self).__init__()
#         self.target=target
#         self.args=args
#         self.num=num
#     def run(self):
#         self.target(self.args,self.num)
# def thisa():
#     p1=r"I:\map"
#     # p2=r"I:\2"
#     # p3=r"I:\3"
#     # p4=r"I:\4"
#     mh1 = MyThread(main,p1,1)
#     # mh2 = MyThread(main, p2, 2)
#     # mh3 = MyThread(main, p3, 3)
#     # mh4 = MyThread(main, p4, 4)
#     mh1.start()
#     # mh2.start()
#     # mh3.start()
#     # mh4.start()
#
# thisa()

