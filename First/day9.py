# import time
# import calendar
# t9= time.clock()
# print("%d"%t9)
# import os
# num = 1
# def sanjiaoxing():
#     for i in range(5):
#         for j in range(i):
#             print('*',end='')
#         print()
# def sanjiaoxing2():
#     for i in range(5):
#         for j in range(5-i):
#             print(' ',end='')
#         for j in range(i):
#             print('*',end='')
#         print()
# while True:
#     time.sleep(1)
#
#     if num == 1:
#         os.system('cls')
#         t=time.asctime(time.localtime())
#         print(t,)
#         sanjiaoxing()
#         num =0
#
#     else:
#         os.system('cls')
#         t = time.asctime(time.localtime())
#         print(t)
#         sanjiaoxing2()
#         num = 1
# t1 = time.time() #获取时间戳
# print(t1)
# t2 = time.gmtime()#获取时间元组
# print(t2)
# t3 = time.localtime()#将时间戳转换为当地时间的元组
# print(t3)
# t4 = time.mktime(t3)#将本地时间元组转化为时间戳
# print(t4)
# t5 = time.asctime(t3)#将本地时间元组转化为字符串
# print(t5)
# t6 = time.ctime() #将时间戳转化位字符串
# print(t6)
# t7 = time.strftime("%Y-%m-%d   %H:%M:%S",t3)
# print(t7)
# time.sleep(5)
# t8 = time.clock()
#
# print("%d"%t8)
# print(calendar.month(2018,12))
# print(calendar.calendar(2099))

def maiyifu():
    num=0

    for i in range(0,5):
        n=0
        print("欢迎光临第%d家店"%(i+1))
        for j in range(0,5):
            if n < 3:
                a= input("要离开吗（y/n）？")
                if a=='y' :
                    print("离店结账。。。。")
                    break
                else:
                    print("买了一件衣服。")
                    num+=1
                    n+=1
            else:
                print('每个只可以买三件衣服，自动结账，进入下一个店')
                break
    print('总共买了%d件衣服'%num)
maiyifu()

list=['一二三 ','四五六','七八九','十十一','十二三']
def  search(list):
    for i in list:
        print(i)
def add():
    name=input("请输入学生姓名：")
    list.append(name)
def delete():
    name = input("请输入学生姓名：")
    list.remove(name)
def select():
    print(list[3:6])
def menu():
    print('** ** ** ** ** ** ** ** 欢迎来到学生管理系统 ** ** ** ** ** *')
    print('                         1、查看学生')
    print('                         2、添加学生')
    print('                         3、删除学生')
    print('                         4、修改学生')
    print('                         5、退出')



def main():
    while True:
        menu()
        a = input('请选择操作：')
        if a == '1':
            search(list)
        elif a == '2':
            add()
        elif a == '3':
            delete()
        elif a == '4':
            select()
        elif a == '5':
            break
        else:
            print("输入错误，请重新输入")
main()