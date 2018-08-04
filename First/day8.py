# def r():
#     global aa
#     aa="ssssss"
# def p():
#     print(aa)
# r()
# p()
# import os
# path = 'D:\学习'
# num=0
# def main(path,num):
#     filename = os.listdir(path)
#     for name in  filename:
#         tpath = os.path.join(path,name)
#         if os.path.isdir(tpath):
#             main(tpath,num)
#         else:
#             num+=1
#             print(name)
#     print("一共这么多文件",num)
# main(path,num)
# 1.	用递归函数默写乘阶3遍
# def jiecheng(n):
#     if  n==1:
#         return 1
#     else:
#         return n*jiecheng(n-1)
# print(jiecheng(5))
# 2.	用递归函数遍历指定的目录
# import os
# def getAll(path):
#     fileList = os.listdir(path)
#     for i in fileList:
#         t = os.path.join(path, i)
#         print(t)
#         if os.path.isdir(t):
#             getAll(t)
#         else:print(i)
#
# getAll('D:\学习')
def pingjunfen():
   list=[]
   sum=0
   for i in range(1,5):
       s=input("请输入第%d个学生的成绩："%i)
       list.append(int(s))
       a = int(s)
       sum+=a
   print("参赛学员的平均分数是%.2f"%(sum/4))
# pingjunfen()

def sangebanji():
    for i in range(1,4):
        print("请输入第%d个班级的成绩*******"%i)
        pingjunfen()
sangebanji()


