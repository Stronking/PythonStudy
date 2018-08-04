from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
def getUrlList():
    url = "http://www.cninfo.com.cn/cninfo-new/disclosure/szse/"
    mheader={"Referer":"http://www.cninfo.com.cn/cninfo-new/disclosure/szse","User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    driver = webdriver.PhantomJS()
    driver.set_window_size(1366, 786)
    driver.get(url)
    data = driver.find_element_by_class_name('ct-line').find_elements_by_tag_name('a')
    # print(driver.page_source)
    # print(data[0:10])\
    # print(len(data))
    urllist=[]
    for i in data:
        urllist.append(i.get_attribute('href'))
        # print(i.get_attribute('href'))
    # print(urllist)
    return urllist


# url = "http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/"
mheader={"Referer":"http://www.cninfo.com.cn/cninfo-new/disclosure/szse","User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

def gethtml(url,header):
    req = request.Request(url,headers=header)
    response = request.urlopen(req)
    html = response.read().decode("utf-8")
    response.close()
    return html
def getPDFurl(html):
    soup = BeautifulSoup(html,"html.parser")
    span = soup.find('div',class_='bd-ct').find_all('iframe')
    # print(html)
    a =span[0].attrs['src']
    print(a)
    return a
def getNmae(html):
    soup = BeautifulSoup(html, "html.parser")
    h2 = soup.find_all('h2')
    name = h2[0].get_text()
    name = name.replace("\t",'')
    # print(name)
    return name
def getPdf(pdfurl,name):
    req = request.Request(pdfurl, headers=mheader)
    response = request.urlopen(req)
    pdf = response.read()
    # n = pdfurl.rfind("/")
    # name = pdfurl[46:]
    name = name.replace("\r\n","")
    path = "D:\新建文件夹\\"+name+'.pdf'
    print(path)
    pdfpath = open(path,'wb')
    pdfpath.write(pdf)
    pdfpath.close()
    print("正在保存",name)
    response.close()

# getNmae(gethtml(url,mheader))

if __name__ == '__main__':
    # num = 1205238301
    # n=1
    # while True:
    #     source = url + str(num)
    #     try :
    #         name = getNmae(gethtml(source,mheader))
    #         getPdf(getPDFurl(gethtml(source,mheader)),name)
    #
    #     except Exception as e:
    #         print("错误信息：",e)
    #         print("爬取遇到错误，或者是下载完成。。。退出循环")
    #     num-=1
    #     n+=1
    urllist = getUrlList()
    for source in urllist:
        try :
            print(source)
            name = getNmae(gethtml(source,mheader))
            getPdf(source,name)

        except Exception as e:
            print("错误信息：",e)
            print("爬取遇到错误，或者是下载完成。。。退出循环")