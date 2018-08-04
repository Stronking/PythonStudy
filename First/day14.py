# li = [1,2,3,4,5,6]
# iter = iter(li)
# while True:
#   try:
#      print(next(iter))
#
#   except StopIteration as iterError:
#         print(iterError)
#         print(iterError.__repr__())
#         # print("hahaha",iterError,'hahahaaha')
#         break


# def InttoChar(k):
#     return str(k)
#
# li=[1,2,5,6,8]
# print(list(map(str,li)))


# from functools import reduce
#
# str='hello world hello teacher hello world'
# list = str.split(' ')
# print(type(list))
# print(list)
# def count(x,y):
#     print(x)
#     if y in x :
#         x[y] +=1
#     else:
#         x[y]=1
#     # print(x)
#     return x
# re = reduce(count,str,{})
# print(re)




        # 用一行python求出 1+2+3+…+100 的和：
        # a = reduce(lambda x,y:x+y,range(1,100+1),)
        #reduce高阶函数内传入lambda匿名函数和range()生成的迭代序列。
        #充分理解reduce函数的实现原理。







# print(a)
# L=[('b',2),('a',1),('c',3),('d',4)]
# a= sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))
# print(a)


# 1.自定义异常，抛出异常，提示您输入的名字长度不应该小于1大于5


# class MyError(BaseException):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         print('name is error')
#         return repr(self.value)
# # try:
# #     raise MyError(2 * 2)
# # except MyError as e:
# #     print('My exception occurred, value:', e.value)
#
# name=input("请输入name：")
# if len(name)>5 or len(name)<1:
#     raise MyError('name')
#
# else:print(name)


# 2. 快速排序
array = [1, 3, 2, 6, 5, 15, 8, 19, 21, 32]
# quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
#     [item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort(
#     [item for item in array[1:] if item > array[0]])

# def quikly(array):
#     l=0
#     h=len(array)
#     p = array[l]
#     while l<h :
#         while l<h and array[h]<p:h-=1
#         if l<h :
#             temp =
#
# print(array)
# def quickSort(L, low, high):
#     i = low
#     j = high
#     if i >= j:
#         return L
#     key = L[i]
#     while i < j:
#         while i < j and L[j] >= key:
#             j = j-1
#         L[i] = L[j]
#         while i < j and L[i] <= key:
#             i = i+1
#         L[j] = L[i]
#     L[i] = key
#     quickSort(L, low, i-1)
#     quickSort(L, j+1, high)
#     return L
# a = quickSort(array,0,len(array)-1)
# print(a)

# def outer():
#     num = 10
#     def inner():
#         nonlocal num
#         num = 100
#         print(num)
#     inner()
#     print(num)
#
# outer()
# map()
# range()

# import  logging
# logging.basicConfig(level=logging.INFO)
# logging.info("aaaaaaa")
# def add(x,y):
#     return x+y
#
# num1 = 1
# num2 = 2
# num3 = add(num1,num2)
# num4=num3
