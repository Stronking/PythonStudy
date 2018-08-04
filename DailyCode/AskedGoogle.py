# code proplem day2
# list1 = [10,15,3,7,2,10]
# k=17
# n = 1
# # for i in range(len(list1)):
# #     num = 0
# #     for j in range(len(list1)-i):
# #             print(n)
# #             n+=1
# #             if list1[i]+list1[j+i]==k:
# #                 print("True Since %d + %d = %d"%(list1[i],list1[j],k))
# #                 num =1
# #                 break
# #     # if num == 1:
# #     #     break
#
# for i in  range(len(list1)-1):
#     for j in range(i+1,len(list1)):
#         if list1[i] + list1[j] == k:
#             print("True Since %d + %d = %d" % (list1[i], list1[j], k))

# code problem day 3
class Node:
    val = ''
    left = ''
    right = ''

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 广度优先遍历解决问题
# 反序列化函数
# def deserialize(li, node):
#     pass
#
#
# # 序列化函数
# def serialize(li, node):
#     # li.append(node.val)
#     # print(type(node))
#     # try :
#     if type(node) != type(['']) or type(node) != None:
#         li.append(node.val)
#         if type(node.left) != type(['']) and type(node.right) != type(['']):
#             li.append(serialize(li, node.left))
#             li.append(serialize(li, node.right))
#         elif type(node.left) == type(['']) and type(node.right) == type(['']):
#             li.append(node.left)
#
#             return node.right
#         elif type(node.left) != type(['']) and type(node.left) == None and type(node.right) == type(['']):
#             li.append(serialize(li, node.left))
#             # print(type(node.right))
#             li.append(node.right)
#         elif type(node.left) == type(['']) and type(node.right) != type(['']) :
#             # print(type(node.left))
#             li.append(node.left)
#             li.append(serialize(li, node.right))
#     else:
#         li.append(node)
#     return li
#     # except :
#     #     print("出错了")
#     #     if node != None:
#     #         li.append(serialize(li, node.left))
#     #         return li
#     #     elif node == None:
#     #         return li
#     #     if node== None:
#     #         li.append(serialize(li, node.right))
#     #         return li
#     #     elif node == None:
#     #         return li
#     #
#     # return li
#
#
# node = Node(['1'], Node(['2'], ['4']), Node(['3'], ['6'], ['7']))
# s = []
# # s.append(None)
# # print(s)
# a = serialize(s, node)
# # s.append('2')
# # s.append('3')
# print(s)
# print(s[4])




#problem day4
# a =[4,5,0,1,-2,-3]
# c = []
# for i in a:
#     if i > 0:
#         c.append(i)
#
# if len(c)==0:
#     print(1)
# else:
#     b = min(c)
#     k = 1
#     while k <= b:
#         if k < b:
#             print(k)
#             break
#         while k == b:
#             c.remove(b)
#             try:
#                 b = min(c)
#             except ValueError as error:
#                 print(b+1)
#             k =  k + 1

def serche(list1):
    num = 1
    while True:
        if num not in list1:
            print(num)
            break
        num+=1
s=[1,1,2,3,4,4,4]

serche(s)

