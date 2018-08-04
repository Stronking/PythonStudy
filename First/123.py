import random

b = random .randint(0, 500);
i=0;
while 1:
    a = input("请输入你猜的数：");
    i+=1;
    if int(a)==b:
        print("猜对了！！")
        break;
    elif int(a) > b :
        print("大了")
    else :
        print("小了")
print("您一共才了"+str(i)+"次");
