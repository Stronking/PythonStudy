# # yz = ([1,2,3],[4,5,6],[7,8,9])
# # print(yz)
# # yz[0].append(4)
# # print(yz)
#
# # zidian = {"a":"123","b":"456","c":"789","d":"abc"}
# # print(zidian.keys())#遍历输出keys
# # print(zidian.values())#遍历输出values
# # print(zidian.items())#输出所有的键值对
# # for k in zidian.keys():
# #     print(k)
# # zidian['a']=456
# # print(zidian.setdefault("e",753))
# # print(zidian)
# #定义字典
# p = {'张三':1000,'王四':2000,'王五':2500,'王六':3000,'马云':15000,'张云':15000}
# #遍历字典
# for dict in p.items():
#     print(dict)
#    #查看所有员工姓名
# print(p.keys())
# #查看所有员工工资
# print(p.values())
# #查看员工工资总和
# sum=0
# for i in p.values():
#     sum+=i
# print("员工工资总和是：%d"%sum)
# #查看姓张的员工的工资总和
# sum=0
# for k,v in p.items():
#     if k[0]=='张':
#         sum+=v
# print("张姓员工工资总和为：%d"%sum)
# #7.查看姓王的员工个数
# sum=0
# for k,v in p.items():
#     if k[0]=='张':
#         sum+=1
# print("张姓员工总数为：%d"%sum)
# #8.把所有员工工资涨1000
# for k,v in p.items():
#     p[k]=v+1000
# print(p)
# # 9.查看5000以上工资的员工有几个
# sum = 0
# for i in p.values():
#     if i >5000:
#         sum+=1
# print("5000以上工资的员工有%d个"%sum)
# # 10.把王五的工资降薪500
# for k,v in p.items():
#     if k=="王五":
#         p[k]=v-500
# print(p)
# # 11.把少于1000的员工开除
# # list=[]
# # for k,v in p.items():
# #     if v<3000:
# #         print(k)
# #         list.append(k)
# # for i in list:
# #     del p[i]
# # print(p)
# # 12.统计姓王的工资和姓张的工资总和分别多少
# sum=0
# for k,v in p.items():
#     if k[0]=='张' or k[0]=='王':
#         sum+=v
# print("张姓员工和王姓员工工资总和为：%d"%sum)
# # 13.新来的员工：马云云 工资200000  添加到字典中
# p.setdefault('马云云',200000)
# print(p)
# # 14.把王五员工替换成马化腾
# p['马化腾']=p.pop('王五')
# print(p)
# # 15.把所有员工姓名加前缀：微软公司
# list=[]
# for name in p.keys():
#     list.append(name)
# for i in list:
#     p['微软公司'+i]=p.pop(i)
# print(p)
# # 16.把姓王的人员前缀修改为腾讯公司
# list=[]
# for name in p.keys():
#     if name[4]=="王":
#         list.append(name)
# for name in list:
#     p['腾讯公司'+name[4:]]=p.pop(name)
# print(p)
# # 17.统计微软公司和腾讯公司各多少人
# m=t=0
# for k,v in p.items():
#     if k.find("微软公司")!=-1:
#         m+=1
#     if k.find("腾讯公司")!=-1:
#         t+=1
# print("微软公司员工总数为%d，腾讯员工总数为%d"%(m,t))
# # 18.统计微软公司姓王的平均工资
#
# # 19.统计微软公司和腾讯公司平均工资各多少
# sumw=sumt=0
# w=t=0
# for k,v in p.items():
#     if k.find('微软')!=-1:
#         sumw+=v
#         w+=1
#     if k.find('腾讯')!=-1:
#         sumt+=v
#         t+=1
# print("腾讯员工平均工资为%.2f,微软员工平均工资为%.2f"%(sumt/t,sumw/w))
#
#
# # 20.把腾讯公司员工全部开除
# print("*****")
# print(p)
# print("*****")
# list=[]
# for k in p.keys():
#     if k.find('腾讯')!=-1:
#         print(k)
#         list.append(k)
# for i in list:
#     del p[i]
# print(p)


# 1.创建中国城市列表（个数自定义）
city=['北京','哈尔滨','石家庄','长春','沈阳']
# 2.遍历列表
# for i in city:
#     print(i)
# 3.把每个城市名称前缀加中国
# for i in range(len(city)):
#     city[i]='中国'+city[i]
# print(city)
# 4.如果遇到”哈尔滨”不输出    遇到"石家庄"停止循环
# city=['北京','哈尔滨','石家庄','长春','沈阳','齐齐哈尔']
# for i in city:
#     if i=='哈尔滨':
#         continue
#     elif i == '石家庄':
#         break
#     else:
#         print(i)
# 5.统计城市名称中有相同字的城市有几个并且打印出来



city=['北京','济南','南京','哈尔滨','石家庄','长春','沈阳','齐齐哈尔']

for i in city: #从第一个开始遍历city标识为i
    for j in range(len(i)): #遍历每个i里面的汉字
        for k in city[city.index(i):]:#从第i个之后开始遍历city的每个列表元素，标识为k
            if i!=k:#不与本身对比
                if k.find(i[j])!=-1:#判断k中有没有i中第j个汉字，如果有打印
                     print(k,i)
            else:continue
citys = ['郑州','大连','菏泽','济南','北京','哈尔滨','石家庄','南京','济宁','齐齐哈尔']
for i in range(0,len(citys)):#遍历citys
    for j in range(i+1,len(citys)):#遍历除了i之后的citys
        for k in list(citys[i]):#将i对应的城市转成list,遍历
            if k in citys[j]:#判断k是否在citys[j]里面
                print(citys[i],citys[j])




# 6.创建list2列表美国城市列表有美国前缀（个数自定义）拼接中国城市列表
# city2=['美国纽约','美国洛杉矶','美国加利福尼亚']+city
# print(city2)

# 7.统计list2列表中美国城市和中国城市各几个
# m=z=1
# for i in city2:
#     if i.find('美国'):
#         m+=1
#     if i.find('中国'):
#         z+=1
# print('中国：%d   美国：%d'%(z,m))
# 8.list2中在美国洛杉矶后面添加美国盛顿城市
# i=city2.index('美国洛杉矶')
# city2=city2[0:i+1]+["美国华盛顿"]+city2[i+1:]
city2.insert(i+1,"美国华盛顿")
# print(city2)

# 9.所有城市加后缀“市”
# for i in range(len(city2)):
#     city2[i]=city2[i]+'市'
# print(city2)

# 10遍历列表list2  查看如果有不带前缀的加前缀，如果有不带后缀的加后缀
# city2=['美国纽约', '洛杉矶市', '美国华盛顿市', '加利福尼亚市', '中国北京', '中国哈尔滨市', '石家庄市', '中国长春市', '中国沈阳市']
# for i in range(len(city2)):
#     if city2[i][0:2]=='中国' or city2[i][0:2]=='美国':
#         pass
#     else:
#         city2[i] = '中国'+city2[i]
#     if city2[i][-1] == '市':
#         pass
#     else:
#         city2[i] = city2[i] + '市'
# print(city2)


#
# 字典技能：
# 11.创建字典 key为学生姓名  value为学生年龄   （学生个数自定义）
sut = {'刘邦':18,'项羽':21,'王五':28,'雨水1':1,'雨水2':1,'雨水3':1,'雨水4':1,'雨水5':1}

# 12.遍历字典
# for i in sut.items():
#     print(i)
# 13.找出年龄大于20的同学并统计个数
# num=0
# for k,v in sut.items():
#     if v>20:
#         print(k)
#         num+=1
# print(num)
# 14.找出姓王的同学并且年龄在10-25之间打印出来
# for k,v in sut.items():
#     if k[0]=='王'and v<=30 and v>=10:
#         print(k,':',v)
# 15.把每个同学年龄加一岁
# for k,v in sut.items():
#     sut[k]=v+1
# print(sut)
# 16.统计学生平均年龄  遇到姓刘的同学不统计
# sum=num=0
# for k,v in sut.items():
#     if k[0]!='刘':
#         sum+=v
#         num+=1
# print(int(sum/num))


# 17.找出学生最高年龄和最低年龄
# list=[]
# for v in sut.values():
#     list.append(v)
# min=min(list)
# max=max(list)
# print(max,min)
# 18.把刘邦的年龄和项羽的年龄互换
# print(sut)
# l=sut.get('刘邦')
# x=sut.get('项羽')
# print(l,x)
# sut['项羽']=l
# sut['刘邦']=x
# print(sut)

# 19.查找是否有张三的学生，如果没有添加  年龄设定为19
# num =0
# for k in sut.keys():
#     if k=='张三':
#         num=1
#         break
# if num!=1:
#     sut.setdefault("张三",19)
# print(sut)

# 20.找出包含“雨”字同学并打印  统计个数  如果个数>5请把他们名字倒序输出
# list=[]
# for k,v in sut.items():
#     if k.find('雨')!=-1:
#         list.append(k)
# if len(list)>=5:
#     print(list[::-1])
# else:print(list)
