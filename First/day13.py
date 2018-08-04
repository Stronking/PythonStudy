# def copyImg(old):
#     oldfile = open(old,'rb')
#     s = oldfile.read()
#     name = old[(old.rfind('/')+1):]
#     print('+++',name)
#     path = old[:(old.rfind('/')+1)]
#     print('-----',path)
#     newName = path + '/[副本]'+name
#     print('000000',newName)
#     newfile = open(newName,'wb')
#     newfile.write(s)
# copyImg("D:/新建文件夹/1.txt")


class Person:
    name=''
    age=0
    height=0
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def eat(self):
        print("Person的吃")
    def drink(self):
        print("person类的喝水")
    def sleep(self):
        print("person类的睡觉")

class Student(Person):
    def studay(self):
        print('student类的学习方法')
    def eat(self):
        print('student类的eat方法')
    def __repr__(super):
        return ('我是%s我的年龄是%d我的身高是%s'%(super.name,super.age,super.height))


class teacher(Person):
    def teach(self):
        print('teacher类的teach方法')
    def sleep(self):
        print('teacher类的sleep方法')
    def __repr__(self):
        return '我是%s我的年龄是%d我的身高是%s'%(self.name,self.age,self.height)



s = Student('aaa',18,180)
print(s.__repr__())
s.eat()
s.sleep()
s.drink()
s.studay()
b = teacher('bbbb',28,178)
print(b.__repr__())
b.eat()
b.sleep()
b.drink()
b.teach()

list=[]
s1=Student('李四',19,175)
s2=Student('张五',17,175)
s3=Student('张三',19,175)
s4=Student('王二',25,175)
s5=Student('王五',19,175)
list.append(s1)
list.append(s2)
list.append(s3)
list.append(s4)
list.append(s5)

def bianli_list(list):
    for i in list:
        print(i.__repr__())




def select(list):
    num = 0
    for i in range(len(list)):
        if list[i].name=='张三':
            num = 1
            list.remove(list[i])
            break
    if num == 0:
        list.append(teacher('张三',21,185))

def update(list):
    num = 0
    for i in range(len(list)):
        if list[i].name=='李四':
            num=1
            list[i].age=28
            break
    if num == 0:
        print('没有李四')

def selectage(list):
    num = 0
    for i in range(len(list)):
        if list[i].age<25 and list[i].age>18:
            num = 1
            print(list[i].age)
    if num == 0:
        list.append(teacher('张三',21,185))
def selectname(list):
    num = 0
    for i in range(len(list)):
        if list[i].name[0]=='张':
            num = 1
            print(list[i].__repr__())
def selectwang(list):
    num = 0
    for i in range(len(list)):
        if list[i].name[0]=='王':
            num = 1
            print(list[i].__repr__())
    print('王姓同学有%d个'%num)
def selecttwo(list):
    num = 0
    for i in range(len(list)):
        if len(list[i].name)==2 and list[i].name[0]!='张':
            print(list[i].__repr__())

# bianli_list(list)
# print('******************************************')
# select(list)
# print('******************************************')
# bianli_list(list)
# print('******************************************')
# select(list)
# print('******************************************')
# bianli_list(list)
bianli_list(list)
print('******************************************')
update(list)
print('******************************************')
bianli_list(list)
print('******************************************')
selectage(list)
print('******************************************')
selectname(list)
print('******************************************')
selectwang(list)
print('******************************************')
selecttwo(list)

