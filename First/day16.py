import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('106.12.28.140', 8888))
while True:
    a = input("shuru :")
    s.send(s)
# #
# # buff=[]
# # while True:
# #     d = s.recv(1024)
# #     if d:
# #         print("第%d字节"%i)
# #         buff.append(d)
# #     else:
# #         break
# # print(buff)
# #
#
# import socket
# def server():
#     num = 0
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind(('10.0.120.249', 9999))
#     sock.listen(100)
#     while True:
#         connection, address = sock.accept()
#         print(connection)
#         print(address)
#         if connection!=None:
#             break
#     try:
#         while True:
#             if num == 1:
#                 sock.listen(5)
#                 connection, address = sock.accept()
#                 print(connection)
#                 print(address)
#                 connection.settimeout(1000)
#                 buf = connection.recv(1024)
#                 # print(buf)
#                 # print(type(buf))
#                 buf = buf.decode("utf-8")
#
#                 if buf == '1':
#                     print("连接成功！")
#                     connection.send(b"successful conection!")
#                     while True:
#                         # s=[]
#                         while True:
#                             buf = connection.recv(1024)
#                             # print(buf)
#                             s = buf
#                             # if buf == None:
#                             #     print("break while")
#                             # print("***")
#                             break
#                         t = s.decode("utf-8")
#                         if t == '我退出客户端了':
#                             print("收到消息：", t)
#                             num = 1
#                             break
#                         else:
#                             print("收到消息：", t)
#                             s = input("发送消息：")
#                             t = s.encode("utf-8")
#                             connection.send(t)
#
#                 else:
#                     continue
#                     # print("连接失败！")
#                     # connection.send(b'please go out!')
#             else:
#                 connection.settimeout(1000)
#                 buf = connection.recv(1024)
#                 # print(buf)
#                 # print(type(buf))
#                 buf = buf.decode("utf-8")
#
#                 if buf == '1':
#                     print("连接成功！")
#                     connection.send(b"successful conection!")
#                     while True:
#                         # s=[]
#                         while True:
#                             buf = connection.recv(1024)
#                             # print(buf)
#                             s=buf
#                             # if buf == None:
#                             #     print("break while")
#                             # print("***")
#                             break
#                         t = s.decode("utf-8")
#                         if t == '我退出客户端了':
#                             print("收到消息：", t)
#                             num = 1
#                             break
#                         else:
#                             print("收到消息：", t)
#                             s = input("发送消息：")
#                             t=s.encode("utf-8")
#                             connection.send(t)
#
#                 else:
#                     continue
#                     # print("连接失败！")
#                     # connection.send(b'please go out!')
#     except socket.timeout:
#         print('time out')
#         connection.close()
# server()
# # import socket
# # import time
#
# # if __name__ == '__main__':
# #     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #     sock.connect(('10.0.120.249', 8001))
# #     time.sleep(2)
# #     sock.send('1')
# #     print
# #     sock.recv(1024)
# #     sock.close()

# import socket
# import time
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(("106.12.28.140",8888))
# # print("启动成功********************")
# # s.connect(('10.0.120.199',8888))
# while True:
#     Server,add = s.recvfrom(1204)
#     print(Server.decode("utf-8"))