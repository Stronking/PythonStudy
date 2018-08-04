# from urllib import request
# from bs4 import BeautifulSoup
# url="https://daikuan.51credit.com/"
# mheaders={'Referer':'https://daikuan.51credit.com/daikuan/bj/list/','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# def getHtml(src):
#     req=request.Request(src)
#     page=request.urlopen(req)
#     html=page.read()
#     # print(html.decode("utf-8"))
#     return html.decode('utf-8')
# def getTitle(html):
#     soup = BeautifulSoup(html,'html.parser')
#     div = soup.find('div',class_='loanList').find_all("ul")
#     print(div)
# def getNum(html):
#     soup = BeautifulSoup(html,'html.parser')
#     div = soup.find('div',class_='ding').find_all('a')
#     s=div[-1].attrs['href']
#     s=s[::-1]
#     s=s[0:2]
#     s=s[::-1]
#     return int(s)
# def getUrlList(num):
#     urllist=[]
#     for i in range(1,num+1):
#         url='https://daikuan.51credit.com/daikuan/bj/list/?page='+str(i)
#         urllist.append(url)
#     return urllist
# def main(url):
#     for i in url:
#         print(i)
#         html=getHtml(i)
#         soup=BeautifulSoup(html,'html.parser')
#         div=soup.find('div',class_='cha_left').find_all('p')
#         print(div)



# getTitle(getHtml(url))
# main(getUrlList(getNum(getHtml(url))))


# print(getHtml(url))
# !/usr/bin/env python
# encoding: utf-8
# !/usr/bin/env python
# encoding: utf-8
# !/usr/bin/env python
# encoding: utf-8
# !/usr/bin/env python
# encoding: utf-8
from requests_html import HTMLSession
import aiohttp
import asyncio
# import hashlib
import os
import re
from traceback import format_exc
from multiprocessing import Pool as ThreadPool
import base64
from cryptography.fernet import Fernet
# 文件下载也要是异步
import aiofiles

# 开始索引数
strat_num = 227000
# 结束索引数
end_num = 250606
key = "X0JxSkg4NFVBQVBPODlUM0VzT1liNnloeWtLcndkSldRT2xURzQ4MEM5RT0="
page_num_pat = re.compile("var picCount.=.(.*?);")
page_id_pat = re.compile("picAy\[0\].=.(.*?);")


def aes_cbc_decrypt(message):
    decrypted_text = Fernet(base64.b64decode(key).decode("utf8")).decrypt(bytes("{}".format(message), encoding="utf8"))
    return decrypted_text.decode("utf8")


# 漫画题目
cosmic_name = "//head//title/text()"
# 漫画id
cosmic_id = "//img[@id='curPic']/@src"
main_url = aes_cbc_decrypt(
    "gAAAAABbNdhqCnxkaJwZ2VL7HUXne_IOic-NsHtE30W-J68oecVmgm0dzO_lLXgTlI7a5_NbUWlkGm7FqLwY81XIBddNWbac4rCgBA9NFAECsNISkhTvdRl4uDSaS6bHY8sbcJJwO13Z")
cosmic_urllist = [main_url.format(i) for i in range(strat_num, end_num + 1)]
print(cosmic_urllist)
pagenum_xpath = "//font[@id='TotalPage']/text()"
full_url = aes_cbc_decrypt(
    "gAAAAABbNdk5FLeX55hOiDAXxgCwwYmGrokYvU3Nd1AOYuOE7OdIEcBdAmSG_Q3kOltealBKMOgUBKDuPUJtzFFPwqoxL-FUip"
    "VNQU-JmBW_K5qxgzTQ3IOla_F61Rscy0fJOaN-mEXKPqrakctyDRN7OVm1LARTMhylQELLuBnJgIT4WXilchg=")  # 漫画的总id，序号的id和格式使用(jpg)
session = HTMLSession()
sema = asyncio.Semaphore(5)
session = HTMLSession()


async def getbuff(url, c_name):
    conn = aiohttp.TCPConnector(verify_ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(url, timeout=60) as r:
            buff = await r.read()
            if not len(buff):
                url = url.replace(".jpg", ".png")
                async with session.get(url, timeout=60) as r2:
                    buff = await r2.read()
            print("nowurl:", url)
            await getimg(url, buff, c_name)


async def run(url, c_name):
    with (await sema):
        await getbuff(url, c_name)


#
def spider(url):
    try:
        req = session.get(url, timeout=15)
        if req.status_code == 200:
            root = req.html
            name = root.xpath(cosmic_name)[0]
            id = page_id_pat.findall(req.text)[0].split('/')[-2]
            max_page = page_num_pat.findall(req.text)[0]
            full_urllist = [full_url.format(id, i, "jpg") for i in range(1, int(max_page) + 1)]
            event_loop = asyncio.get_event_loop()
            tasks = [run(url, name) for url in full_urllist]
            results = event_loop.run_until_complete(asyncio.wait(tasks))
    except:
        print(format_exc())


async def getimg(url, buff, c_name):
    # 题目那层目录
    filepath = os.path.join(os.getcwd(), "/comics_images", c_name)
    # 如果标题太长就转md5，然后单独启动一个text写入内容为标题
    md5name = hashlib.md5(c_name.encode("utf-8")).hexdigest()
    filepath2 = os.path.join(os.getcwd(), "/comics_images", md5name)

    id = url.split('/')[-1]
    image_id = os.path.join(filepath, id)
    image_id2 = os.path.join(filepath2, md5name)

    # 题目层目录是否存在
    if not os.path.exists(filepath) and not os.path.exists(filepath2):
        # 文件是否存在
        try:
            print(filepath)
            os.makedirs(filepath)
        except:
            print(filepath2)
            os.makedirs(filepath2)
            image_id = image_id2
            # with open(os.path.join(filepath2,"title.txt"),"w",encoding="utf-8") as fs:
            #      fs.write(c_name)
            fs = await aiofiles.open(os.path.join(filepath2, "title.txt"), 'w')
            await fs.write(c_name)

    if not os.path.exists(image_id) and not os.path.exists(image_id2):
        print("savepath:", image_id)
        # with open(image_id, 'wb') as fs:
        #        fs.write(buff)
        f = await aiofiles.open(image_id, 'wb')
        await f.write(buff)


if __name__ == '__main__':
    with ThreadPool(4) as pool:
        pool.map(spider, cosmic_urllist)
try:
    raise