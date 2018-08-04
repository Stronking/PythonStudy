import random
import os

user = {}


def menu():
    print("******************************")
    print("********\t1、 注册\t**********")
    print("********\t2、 登陆\t**********")
    print("********\t3、 抽奖\t**********")
    num = input("请选择操作：")
    if int(num) == 1:
        reg()
        goon()
    elif int(num) == 2:
        main()
    elif int(num) == 3:
        rand('admin')
    else:
        print("输入错误，请重新输入。")


def reg():
    print("**********\t欢迎注册抽奖系统\t**********")
    name = input("\t请输入用户名：")
    pwd = input("\t请输入 密  码：")
    pwd2 = input("\t请输再次入密码：")
    if pwd == pwd2:
        user.setdefault(name, pwd2)


def main():
    num = 0
    print("**********\t欢迎登陆抽奖系统\t**********")
    while 1:
        name = input("\t请输入用户名：")
        pwd = input("\t请输入 密 码：")
        if pwd == user[name] :
            os.system("cls")
            goon()
            break
        else:
            if num == 2:
                print("您输入次数已达最高次数，系统自动冻结您的账户！")
                exit()
            num += 1
            print("对不起，用户名或密码错误，请从新输入！您还有", 3 - num, "次机会！")
            continue


def rand(name):
    print("*********欢迎%s进入抽奖系统**********" % name)
    num = 3
    while num > 0:
        vnum = input("请输入会员号(必须是四位)：")
        if len(vnum) == 1:
            t = random.randint(1, 3)
            if int(vnum) == t:
                print("恭喜您，中奖了！")
                break
            else:
                print("本次中将号码是:", t)
                num -= 1
                print("对不起，您没有中奖,还有%d次机会！" % (num))

        else:
            print("对不起，您输入的会员号有误。")
            continue
def goon():
    a=input("是否继续（y/n）?")
    if a == "y":
        menu()
    else:
        print("系统退出。。。。。。")
        exit()

menu()
