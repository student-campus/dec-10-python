#class and objects ,method(function)
'''
class Test():
    a=10
    b=11
'''
class Math():
    a=10
    b=11
obj1 = Math()
obj1.c = 100
print(obj1.c)

class Add():
    a=17
    b=50
    def add(self):
        return self.a+self.b 
obj = Add()
print(obj.add())

class Sub():
    f=56
    g=24
    def subtrac(self):  #self use attribute to whole class
        return self.f-self.g
obj = Sub()
print(obj.subtrac())

class Mul():
    r=45
    s=54
    def mult(self):
        return self.r *self.s
obj = Mul()
print(obj.mult())

#constructor __init__(self)   call itself doesnot return
class Sut():
    def __init__(self,a,b): 
        self.a =a 
        self.b= b
        print("hello iam, here.")
    def func (self):
        return self.a/self.b
obj = Sut(1,2)#values only pass through
print(obj.fun())
for i in range(1,10,-1):
    print(i)