# str='http://bpic.588ku.com/back_pic/05/51/43/305ae1e9303278a.jpg    '
# a=str.rindex('/')
# print(str[a:])
# print(str[::-1])
# for i in reversed(str):
#     print(i,end='')
#
# print(str.rindex('i'))
# print(str.find('a'))
# print(str.replace("/",''))
# print(str.strip())
# print(str.lstrip("h"))
# print(str.rstrip("g"))
# list=[[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16,'a'],[17,18,19]],[[21,22,23],[24,25,26],[27,28,29]]]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             print(list[i][j][k],end=',')
#         print('\t')
#     print()
# print(list)
# print(list.count('a'))


namelist = ['张一','李二','张三','张刚','王小刚','张六']#创建一个列表
# for name in namelist:#遍历列表
#     if name[0]=='张':   #打印所有姓张的同学
#         if name == '张四': #如果遇到张四 不打印
#             continue
#         elif name == '张五': #如果遇到张五  退出遍历
#             break
#         else:
#             print(name)
#     else:
#         continue
#
# for name in namelist: #将所有姓张的同学改成姓刘
#     print(name[0]=='张')
#     if name[0]=='张':
#         i=namelist.index(name)
#         namelist[i]=name.replace('张','刘')
#     else:
#         continue
# print(namelist)

# for name in namelist: #找到李二同学并删除
#     if name == '李二':
#         i=namelist.index(name)
#         namelist.pop(i)
#     else:continue
# print(namelist)
# count = 0  #找到"刚"并统计多少个
# for name in namelist:
#     # for i in name:
#     #     if i=='刚':
#     #         count+=1
#     if name.find("刚")!= -1:
#         count+=1
# print(count)
# #将所有姓名前面加1808班
# for name in namelist:
#     i = namelist.index(name)
#     namelist[i]='1808班'+name
# print(namelist)
# # 11.创建列表五个1809班级同学姓名列表并与1808班级列表拼接生成新的列表list3
list1= ['1808班张一','1808班李二','1808班张美','1808班张刚','1808班王小刚','1808班张六']
list2=['1809班老大','1809班老二','1809班王老三','1809班老四','1809班王老五']
list3=list1+list2
print(list3)
# # 12.在list3列表中查找1809的学生打印出来
# for name in  list3:
#     if name.find("1809")!=-1:
#         print(name)
# # 13.list3查找1808班级姓王的同学姓名打印出来
# for name in list3:
#     if name.find('1808')!=-1:
#         if name.find('王')!=-1:
#             print(name)
# # 14.list3查看1808和1809班级姓王的同学各几个
# num1808=0
# num1809=0
# for name in list3:
#     print(name)
#     if name.find('1808')!=-1:
#         if name.find('王')!=-1:
#             num1808+=1
#             print(name)
#     elif name.find('1809')!=-1:
#         if name.find('王')!=-1:
#             num1809+=1
#             print(name)
#     else:continue
# print(id(num1808),id(num1809))
# print("1808班王姓同学有%d个，1809班王姓同学有%d个"%(num1808,num1809))
# # 15.list3中姓名包含"美"的同学不打印，并替换成"美美"
# for name in list3:
#     if name.find('美')!=-1:
#         i=list3.index(name)
#         list3[i]=name.replace('美','美美')
# print(list3)
# # 16.list3倒序打印出来
# print(list(reversed(list3)))
# # 17.打印list3中3-6位置的同学   并且姓名全部修改成"马化腾"
print(list3[2:5])
list3[2:5]=['马化腾']*3
print(list3)
# # 18.查看list3中姓名两个字和三个字的学生各几个
# num2=0
# num3=0
# for name in list3:
#     print(name[5:])
#     if len(name[5:])==2:
#         num2+=1
#     elif len(name[5:])==3:
#         num3+=1
#     else:pass
# print("两个字的有%d个，三个字的有%d个"%(num2,num3))
 # 19.list3找出所有"马化腾"在列表中的位置没有的话给出提示
# num = 0
# for name in list3:
#     if name=='马化腾':
#         print(list3.index(name))
#         num+=1
# if num<=0:
#     print("没有这个名称")
num=0
for x in range(1,len(list3)):
    if "马化腾" in list3[x]:
        print(x)
        num+=1
if num <= 0:
    print("没有这个名称")
# 20.list3中找出姓“刘的同学”并把他们的姓名倒序输出,找不到给出提示






