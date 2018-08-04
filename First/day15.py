import re
#
# s='aaaaaaaaaaaaaa agen@1a.com aaaaaaaaaaaaaaaaaaaaaa1211234567891aaaaaaaaaaaaa'
#
# print(re.search("\w{4,18}[@]\w+[.][a-zA-Z]+",s))
# qq="363133710"
# t="010-12345678"
# print("phone",re.findall("^[1][0-9]{10}$",s))
# print("qq",re.search("[1-9][0-9]{5,9}",qq))
# print("cell phone",re.search("^\d{3}-\d{8}$",t))
# s="ssa_saa"
# print(re.search("\w{6,12}",s))

class error_2(Exception):
    def __init__(self,err):
        super().__init__(self)
        self.err=err

try:
    QQ=input('请输入QQ号')
    if re.search("^[1-9]\d{6,11}$",QQ)!=None:
        print(QQ)

    else:
        raise error_2('输入有误')

except error_2 as e:
    print(e.err)

# s=input('请输入QQ号')
# print(type(s))
# print(re.search("[1-9][0-9]{5,10}",s))