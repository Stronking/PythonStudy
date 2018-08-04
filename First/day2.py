
""" 打印1-100之间的偶数
for num  in range(2,101):
    if num%2==0:
        print(num)
    else:
        continue;
"""
"""  打印1-100以内奇数并且能被3整除

for num in range(3,101):
    if num%3==0 and num%2!=0 :
        print(num)
    else:
        continue

"""
"""  打印乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end="\t")
    print()
"""
"""
  # 打印等腰三角形
for i in range(1,7):
    for a in range(7-i):
        print(" ",end="")
    for b in range(2*i-1):
        print("*",end="")
    print()
#打印到等腰三角形
b = num = 8
while num>=0:
    a=num*2-1
    c = b - num
    while c > 0:
        print(" ", end="")
        c -= 1
    while a>0:
        print("*",end="")
        a-=1
    num-=1
    print()




"""


""" 打印矩形
for i in range (5):
    for j in  range(8):
        print("*",end="\t")
    print()
"""

"""
打印1-100之间的偶数
def num():
    num=1
    while num<=100:
        if num%2==0:
            print(num)
        num+=1
    return "完成"
print(num())
"""
"""
打印正直角三角形
num = 1
while num<=5:
    t = 1
    while t<=num:
        print("8",end="")
        t+=1
    print()
    num+=1
   
剪刀石头布
import random
flag = True
while flag:
    r = random.randint(1, 3)
    c=input("请选择：1、布 2、剪刀 3、石头")
    if int(r)==3 and int(c)==1:
        print("你赢了！")
        flag=False
    if int(r)>=int(c):
        print("再来一次！")
    else :
        print("你赢了！")
        flag = False

打印倒直角三角
num=5
while num>0:
    a=num
    while a>0:
        print("*",end="")
        a-=1
    num-=1
    print()

打印1-100之间   20个偶数
num = 1
i=0
while num<100:
    if num%2==0:
        print(num)
        i+=1
    if i==20:
        break
    num+=1
    """
"""

def main():
    num = 0
    print("**********\t欢迎登陆航空系统\t**********")
    while 1:
        name = input("\t请输入用户名：")
        pwd = input("\t请输入 密 码：")
        if name == "admin" and pwd == "123456":
            print("   登入成功！欢迎", name)
            break
        else:
            if num == 2:
                print("您输入次数已达最高次数，系统自动冻结您的账户！")
                break
            num += 1
            print("对不起，用户名或密码错误，请从新输入！您还有", 3 - num, "次机会！")
            continue
main()


"""

num=1
while num<=9:
    a = 1
    while a<=num:
        print(a,"*",num,"=",a*num,end="\t")
        a+=1
    num+=1
    print()
""""
num = 1
while num<=50:
    if num%2==0 and num<=40:
        print(num)
    num+=1


print("奔跑……")
while True:
    a=input("小明喝水吗？")
    if a=="不喝":
     print("继续奔跑……")
    else :
        break
        """




























