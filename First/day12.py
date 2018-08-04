class man:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age


    @name.setter
    def name(self,name):
        if len(name)>=4:
            print('名字非法')
        else:
            self.__name=name
    @age.setter
    def age(self,age):
        if age>130:
            print('年龄非法')
        else:
            self.__age=age


m=man('hahaha',1200)


