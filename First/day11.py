class one:
    __name=''
    __age=0
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    @classmethod
    def talk(self):
        print("说话")
    def eat(self):
        print('one 吃饭')
class two(one):
    def eat(self):
        print('two 喝奶粉')
o=one()
o.eat()
o.talk()
t = two()
t.talk()
t.eat()
super(two,t).eat()
t.setName('hahaha')
print(t.getName())
