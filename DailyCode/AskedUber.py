# code problem day1
list1 = [3,2,1]
# def chengji(x):
#     return x*chengji(x)
# for i in range(len(list)):
list2 =[]
list3=[1,1,1]


list1 = [3,2,1]
for i in list1:
    sum = 1
    for j in list1:
        if i != j:
            sum*=j
    list2.append(sum)
print(list2)


for i in range(len(list1)):
    sum = 1
    for j in range(len(list1)):
        if i != j:
            # print(list1[j])
            sum*=list1[j]
    list3[i]=sum
print(list3)



list1 = [3,2,1]
list2 =[]
for i in range(len(list1)):
    sum = 1
    for j in list1:
       sum*=j
    sum = sum//list1[i]
    list2.append(sum)
print(list2)



