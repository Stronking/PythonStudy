from urllib import request
url='http://www.baidu.com'
req=request.Request(url,headers={})
page = request.urlopen(req)
print(page.read())