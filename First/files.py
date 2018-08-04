# import os,uuid
# import shutil
#
#
# newpath='I:\Tencent\\123'
# tpath = input("请输入路径：")
# def main(tpath):
#     num = 0
#     list = os.listdir(tpath)
#     for i in list:
#         t = os.path.join(tpath, i)
#         if os.path.isdir(t):
#             if os.listdir(t) == []:
#                 os.rmdir(t)
#             else:
#                 num += main(t)
#         else:
#
#             x = i.rfind('.')
#             m = i[x + 1:]
#             n = i[x:]
#             if m == 'jpg' or m == 'png' or m == 'mp4' or m=='txt'or n == 'temp':
#                 # print("**************")
#                 name=uuid.uuid1()
#                 copy(t,newpath,str(name))
#                 num+=1
#                 # print("**************")
#
#             else:
#                 print('*******************************************')
#                 print(i)
#                 print('*******************************************')
#                 # os.remove(t)
#
#     return num
#
#
#
#
#
#
# def copy(old,new,name):
#     path=new+'\\'+name+'.mp4'
#     if os.path.isdir(new):
#         shutil.copy(old,path)
#         print(path)
#     else :
#         os.mkdir(new)
#         print(path)
#         shutil.copy(old,path)
#
#
#
# print(main(tpath))

# def decode(key):
# #     m=''
# #     for i in key:
# #         n = ord(i) + 5
# #         t = chr(n)
# #         m = m + t
# #     return m
# #
# # print(decode("jie mi chu lai ni jiu li hai le"))
print(1024 * 1024 * 1024 // 4 // 3)