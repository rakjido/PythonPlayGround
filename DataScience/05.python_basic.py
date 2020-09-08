# -*- coding: utf-8 -*-

var = 100

print("globals()['var'] : {} ".format(globals()['var']))

def funct(x):
    return x


print("funct(100) : {} ".format(funct(100)))
print("globals()['funct'] : {} ".format(globals()['funct']))
print("globals()['funct'] is func : {} ".format(globals()['funct'] is funct))

# *args : 여러 인자를 튜플로 묶어서 할당 {'args':(1,2,3,4,5)}
# **kwargs : dictionary에 key와 value로 저장 {'kwargs':{'k':1,'T':2}}

*a, b = (1, 2, 3, 4)
print(a)
print(b)

def var_arg(*args):
    print(args)
    return sum(args)

arg = var_arg(1,2,3,4,5,6,7,8,9,10)
print(arg)

def var_kwargs(**kwargs):
    print(kwargs)
    return sum([*kwargs.values()])

kwarg = var_kwargs(a=1, b=2)
print(kwarg)

def var_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    args = list(args) + [*kwargs.values()]
    return sum(args)

args_kwargs = var_args_kwargs(1,2,3,4,5,a=1,b=2)
print(args_kwargs)


#---------------------------------------------

class Klass(object):  # (object) : object 상속 
    # __private_variable : "__"를 앞에 붙이면 private
    # _protected_variable : "_"를 앞에 붙이면 protected

    def __init__(self, name):
        self.name = name 
    
    def getName(self):
        return self.name 



k = Klass("Object Create")
print(k.name)
print(k.getName())

print(isinstance(k, Klass))

# getName이 method라는 걸 확인 할 수 있다 
print(Klass.__dict__)

print(Klass.__init__)
print(k.__init__)

class hello:
    num = 10

    @staticmethod
    def calc(x, y):
        return x + y

    @staticmethod
    def add_calc(x, y):
        return hello.num + x + y

    @classmethod
    def add(cls, x,y):
        return x+y

    @classmethod
    def add_num(cls, x, y):
        return cls.num + x + y

print(hello.calc(10, 20))
print(hello.add_calc(1,3))

print(hello.add(1,3))
print(hello.add_num(1,3))
