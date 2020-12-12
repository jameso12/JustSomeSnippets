# the rest...
'''
def foo(a, b, *args, **kwargs): 
    # * saves extra positional arguments as a tuple
    # **saves extra positional arguments as a dictionary
    # * forces keyword only arguments to its left
    # *args counts for what is above ^^

    print(a,b)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, kwargs[key])

foo('james', 'odalz')

foo(1, 2, 'si', 'no', ['ai', 'q'], john = 'loco', maria = 'pero')

# unpacking lists, tuples
def fii(a, b, c):
    print(a,b,c)

l = [1, 2, 3]
fii(*l)

# unpacking dictonries
# dictionary must have same keys as the parameters
def fido (a, b, jon):
    print(a,b,jon)

d = {'a': 3, 'b': 'john', 'jon': True}
fido(**d)


def loli():
    mani = misu
    print(mani)

def lilo():
    minu = misu
    print(minu)
    
misu = 0
loli()
lilo()
# '*' unpacks things like lists and tuples

mimo = ['la', '1', 3, 'james']
first, *things, name = mimo
print(first)
print(things)
print(name)

myt = (1,2)

mn =[*mimo, *myt]
print(mn)

d1 = {'a':1, 'b':2}
d2 ={"c": 3, "d": 4}
d3 ={**d1, **d2}
print(d3)
'''

# copying
# shallow copy: one level deep, just more refferences
import copy
org = [4, 3,2,5]
cpy = copy.copy(org)

print(org)
cpy.append(10)
print(cpy)

# actual copy

cpy=copy.deepcopy(org)
print(cpy)

# usefull for costume objects

class Person:
    def __init__(self, name,age):
        self.name =name
        self.age = age

p1 = Person("Alex", 27)

p2 = p1
p2.age = 28

print(p1.age) # 28
print(p2.age) # 28

# but if we used deep copy
p2 = copy.deepcopy(p1)

p2.age = 200
print(p1.age)
print(p2.age)

# context managers
# allow you to allocate and release content when you want to
# like:
# with open() as someVarName:
# it closes the file or content even if an exception would occur

# to create our own context manager, for things like costum classes:

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
            '''
        if exc_type is not False: # if some exception happens
            print('hanel')
            '''
        print("closed")
        return True 
        # you want to return true so that the program does not stop and keeps going
        # in this case, so that 'print('yes')' is executed

with ManagedFile('somefile.txt') as f:
    f.write('hello!')
    f.bole()

print('yes')

from contextlib import contextmanager


@contextmanager # this allows this to be used with 'with'
def open_managed_file(filename): 
    f = open(filename, 'w')
    try:
        yield f # 'suspends in execution', this allows one to tamper with the file
    finally:
        f.close()

with open_managed_file('somefile.txt') as f:
    f.write('hellooooo')