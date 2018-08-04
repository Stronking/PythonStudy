# class Dog:
# #     name=""
# #     age=""
# #     color=""
# #     sex=''
# #     weight=''
# #     def __init__(self,name,age,color,sex,weight):
# #         print('正在时间初始化')
# #         self.name =name
# #         self.age = age
# #         self.color = color
# #         self.sex = sex
# #         self.weight = weight
# #     def eat(self):
# #         print("正在吃饭。。。。")
# #     def drink(self):
# #         print("正在喝水")
# #     def sleep(self):
# #         print("正在睡觉")
# #     def run(self):
# #         print("正在跑步")
# #     def work(self):
# #         print("正在工作")
# # d1=Dog('狗一',1,'黄','公',20)
# # d2=Dog('狗二',2,'红','母',20)
# # d3=Dog('狗三',3,'绿','公',20)
# # d4=Dog('狗四',4,'青','公',20)
# # d5=Dog('狗五',5,'蓝','母',20)
# # list=[d1,d2,d3,d4,d5]
# # for i in list:
# #     print("****************")
# #     print(i.weight)
# #     print(i.sex)
# #     print(i.name)
# #     print(i.color)
# #     print(i.age)

# class stu:
#    name=''
#    height=''
#    ID=''
#    sex=''
#    def __init__(self,name,height,id,sex):
#        self.name=name
#        self.sex=sex
#        self.height=height
#        self.ID=id
#    def study(self):
#        print('学习')
#    def sleep(self):
#        print('睡觉')
#    def run(self):
#        print("跑步")
#    def eat(self):
#        print('吃饭')
# l=[]
# for i in range(4):
#     n=input('请输入姓名：')
#     s = input('请输入体重：')
#     h = input('请输入性别：')
#     st=stu(n,h,i,s)
#     l.append(st)
# for i in l :

#     print('********************')
#     print(i.ID)
#     print(i.name)
#     print(i.height)
#     print(i.sex)
#     i.sleep()
class Dog:
    name = ''
    age = ''

    def __init__(self):
        print('88888888*********************')
        name = 'jeck'
        age = '19'

    def age(self):
        print(self.age)

    def name(self):
        print(self.name)


d = Dog()
d.age()
d.name()
