import wave  #导入wave   Python自带
from pyaudio import PyAudio,paInt16  #导入pyaudio模块内的类和常量    安装方法pip install pyaudio
from  aip import AipSpeech   #导入百度AI   SDK   安装方法   pip  install baidu-aip
import time
#paInt16
framerate=16000  #全局变量采样率
NUM_SAMPLES=2000 #录音字节
shengdao=1   #采样声道
zijie=2
TIME=5 #录音时长
"""

保存录音函数
sava_wava_file

"""

def save_wave_file(filename,data):
    wf=wave.open(filename,'wb') #以二进制形式写入
    wf.setnchannels(shengdao)#声道
    wf.setsampwidth(zijie)#采样字节 1 or 2
    wf.setframerate(framerate)#采样频率 8000 or 16000
    wf.writeframes(b"".join(data))#从文件末尾添加数据
    wf.close() #关闭文件，释放缓冲

"""

录音函数
my_record

"""

def my_record():
    pa=PyAudio() #实例化操作wave流的类
    stream=pa.open(format = paInt16,channels=1,rate=framerate,input=True,frames_per_buffer=NUM_SAMPLES)#打开音频流，格式、频道、采样率、输入、每次的大小
    my_buf=[] #空数据列表，存储流。
    count=0  #计数，退出录音循环
    print("请说话：")
    t1=time.clock()
    while count<TIME*5:#控制录音时间  3*5*2000 =30000
        string_audio_data = stream.read(NUM_SAMPLES)#一次性录音采样字节大小
        my_buf.append(string_audio_data) #每次将数据追加到存储数据的list中
        count+=1
        print('.')
    t2=time.clock()
    print('一共录音',t2-t1,'秒')
    save_wave_file('D:/123/01.wav',my_buf) #将数据保存到路径文件中。
    stream.close() #关闭流
my_record()  #调用函数
""" 你的 APPID AK SK """
APP_ID = '11499799'  #从百度获取属于你自己的
API_KEY = '4bewlVoZwvNUsApp3OSQs62H'#从百度获取属于你自己的
SECRET_KEY = 'SSn5DomfKwmQHywyDk8zHUGpGB6OantF'#从百度获取属于你自己的
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY) #获取链接。。。。
# pa = input("输入语音文件：")

"""

读取音频函数
getWAV

"""

def getWAV(path):
    with  open(path,'rb') as fi:  #打开音频文件，并命名别名  fi
        return fi.read()   #返回读取的音频数据
"""

语音识别函数

"""

def AIaudio():
    Json = client.asr(getWAV('D:/123/01.wav'),'pcm',16000,None)  #请求链接，上传数据，获取返回数据。
    # print(Json)
    try:
        s = Json["result"]
        print(s)
        return s[0]
    except KeyError:
        print('音频质量或者是其他错误。。。。')
        return 0

AIaudio()