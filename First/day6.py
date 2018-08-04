import random

def jia(num1, num2):   #实现加函数
    return num1 + num2


def jian(num1, num2):#实现减函数
    return num1 - num2


def cheng(num1, num2):#实现乘函数
    return num1 * num2


def chu(num1, num2):#实现除函数
    return num1 / num2


def dayinsanjiaoxing():  #实现打印直角三角形  函数
    num=input("请输入打印三角形的行数：")
    for i in range(int(num)):
        for j in range(i+1):
            print("*",end="")
        print()


def test():
    print(1)
    return test2()
def test2():
    print(2)
    return test()


stuList = ['张三','李四','王五','李白']
def bianliliebiao(list):
    for i in list:
        print(i)
def xiugaixingming(namelits,oldname,newname):
    print(namelits)
    for i in range(len(namelits)):
        if namelits[i] == oldname:
            namelits[i]=newname
    print(namelits)
def chazhaoxingming(namelist,name):
    if name in namelist:
        print("找到")
    else:print("没有找到")
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
def main():
    num = 0
    print("**********\t欢迎登陆抽奖系统\t**********")
    while 1:
        name = input("\t请输入用户名：")
        pwd = input("\t请输入 密 码：")
        if name == "admin" and pwd == "123456":
            print('登陆成功')
            break
        else:
            if num == 2:
                print("您输入次数已达最高次数，系统自动冻结您的账户！")
                break
            num += 1
            print("对不起，用户名或密码错误，请从新输入！您还有", 3 - num, "次机会！")
            continue

def chazhaozhidingweizhi(name,num1,num2):
    print(name[num1-1:num2])
def chazhaoxing(name,xing):
    for i in name:
        if xing in i :
            print(i)
def 删除学生(namelist,name):
    num=0
    for i in range(0,len(namelist)):
        if name==namelist[i]:
            del namelist[i]
            num=1
            print('删除成功')
            break
    if num==0:
        print('没有找到')
def danzitongji(name,i):
    num = 0
    for x in name:
        if i in x:
            num+=1
    print("有%d个"%num)

# 13.输入班级号拼接名字函数   如果判断有班级号的学生  把班级号替换


# 14.创建字典key为:学生姓名,value为：成绩  五个学生即可

stu={'AAA':90,'BBB':80,'CCC':80,'DDD':75,'EEE':70}
# 以下关于操作字典的函数：
# 15.查看学生姓名和成绩函数

def bianli(stu):
    for i in stu.items():
        print(i)
# 16.统计成绩平均分函数
def pingjun(stu):
    sum=0
    for v in stu.values():
        sum+=v
# 17.根据分数范围找出学生函数
def genjufenshuchazhaoxuesheng(stu,num):
    for k,v in stu.items():
        if v==num:
            print(k)
# 18.指定的成绩范围  可以指定的分  函数
def zhidingdechengjifanwei(stu,min,max):
    for k,v in stu.items():
        if v>=min and v<=max:
            print(k)
# 19.指定字数 绩 查看学生姓名和成


# 20.根据姓氏,成绩查看学生姓名和成绩




# chazhaoxingming(stuList,'李四1')
# xiugaixingming(stuList,"李四",'李思思')
# chazhaozhidingweizhi(stuList,1,2)
# chazhaoxing(stuList,'李')
x=input("姓名：")
删除学生(stuList,x)

# danzitongji(stuList,"李")
# bianli(stu)
# genjufenshuchazhaoxuesheng(stu,80)
# zhidingdechengjifanwei(stu,80,100)