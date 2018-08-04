# from aip import AipSpeech
# APP_ID = '11499799'
# API_KEY = '4bewlVoZwvNUsApp3OSQs62H'
# SECRET_KEY = 'SSn5DomfKwmQHywyDk8zHUGpGB6OantF '
# client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# with open("D:/1.txt",'r') as txt:
#     st = txt.read()
#     print(st)
#     i = 0
#     if st !=  None:
#         result  = client.synthesis(st, 'zh', 1, {'vol': 10,})
#         if not isinstance(result, dict):
#             with open('auido'+str(i)+'.mp3', 'wb') as f:
#                 f.write(result)
#         i+=1
import time
print(time.time())