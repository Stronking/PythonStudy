# for s in "hello world":
#     if s=="w":
#         break
#     print(s,end="")
# else :
#     print("没有遇到")


# list = ['a','b','c','d','e']
# for x in list:
#     if x=='b':
#         continue
#     print(x)


# for i in range(1,6):
#     for a in range(i):
#         print("*",end="")
#     print()

# for i in range(1,6):
#     for a in range(1,6):
#         print("*",end="")
#     print()


# for i in range(1,101):
#     if i%2==0:
#         print(i)

# for i in range(1,51):
#     if i%2==1 and i%3==0:
#         print(i)

# num=1
# for i in range(1,6):
#     num*=i
# print(num)

# for i in range(1,4):
#     for k in range(1,4-i):
#         print(' ', end='')
#     for j in range(i*2-1,):
#         print('*',end='')
#
#
#     print()

#
# a=3**3
# b=pow(3,3)
# print(a,b)
# x=3.111123456789
# print(x)
# print(round(x,6))
# import math
# print(math.ceil(1.111))
# print(math.floor(1.111))
# print(math.modf(1.1111111112111))
# print(math.sqrt(9))
# import random
#
# list = [1, 2, 5, 6, 7, 9, 12, 56, 79]
# a = random.choice("abcdef")
# b = random.choice(range(3))
# print(b)
# random.shuffle(['a','b','c','d'])
# random.uniform(10,100)
# a=random.randint(10,100)
# b="1+2"
# print("我叫%s，我的年龄是%d"%("yyyy",15))
# print(eval(b))
# list.append(3)
# print(list)
# del list[2]
# print(random.choice(range(1000,10000)))


import random
import os
user={}

def menu():
    print("******************************")
    print("********\t1、注册\t**********")
    print("********\t2、登陆\t**********")
    print("********\t3、抽奖\t**********")
    num= input("请选择操作：")
    if int(num)==1:
        main()
    elif int(num)==2:
        main()
    elif int(num)==3:
        main()
    else:
        print("输入错误，请重新输入。")

def reg():

    print("**********\t欢迎注册抽奖系统\t**********")
    name = input("\t请输入用户名：")
    pwd = input("\t请输入 密  码：")
    pwd2= input("\t请输再次入密码：")
    if pwd==pwd2:
        user.setdefault(name,pwd2)


def main():
    num = 0
    print("**********\t欢迎登陆抽奖系统\t**********")
    while 1:
        name = input("\t请输入用户名：")
        pwd = input("\t请输入 密 码：")
        if name == "admin" and pwd == "123456":
            os.system("cls")
            rand(name)
            break
        else:
            if num == 2:
                print("您输入次数已达最高次数，系统自动冻结您的账户！")
                break
            num += 1
            print("对不起，用户名或密码错误，请从新输入！您还有", 3 - num, "次机会！")
            continue

def rand(name):
    print("*********欢迎%s进入抽奖系统**********"%name)
    num=3
    while num>0:
        vnum=input("请输入会员号(必须是四位)：")
        if len(vnum)==1:
            t=random.randint(1, 3)
            if int(vnum) == t :
                print("恭喜您，中奖了！")
                break
            else:
                print("本次中将号码是:",t)
                num -= 1
                print("对不起，您没有中奖,还有%d次机会！"%(num))
        else:
            print("对不起，您输入的会员号有误。")
            continue

menu()


# import random
# a=random.randint(10000,100000)
# print(a)
# 随机1-200之间的数
# a=random.choice(range(1,201))
# print(a)
# 遍历字符串"helloworld" 如果遇到不打印l ,遇到w退出循
# s="helloword"
# for x in  s:
#     if x=='w':
#         break
#     elif x=='l':
#         continue
#     else:
#         print(x)
# list=['a','a','a']
# for a in list:
#     list.append('a')
#     print(len(list))
#     # del list[0]
# list=['a','a','a',"a"]
# for a in list:
#     list.append("a")
#     print(list)
#     list.remove("a")
#     print(list)
