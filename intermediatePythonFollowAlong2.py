import random
r = random.random()
r = (r * 1000) // 10
print(r)

# decorators
def mydec(func):

    def wrapper():
        print("Hello, from wrapper")
        func()

    return wrapper

def nemo():
    print('Nemo')

nemo()

# to decorate 

nemo = mydec(nemo)
nemo()

# another way to do this is 

def mydec(func):

    def wrapper():
        print("Hello, from wrapper")
        func()

    return wrapper

@mydec
def nemo():
    print('Nemo')

nemo()


# another example

def somedec(func):
    def wrapper(x):
        func(x)
        print('done inside wrapper')
    return wrapper

@somedec
def mini(x):
    print( x + 5)

mini(5)
print(mini.__name__)
# to preserver the information of the mini function you need
print("keeping function identity")
import functools

def somedec(func):
    @functools.wraps(func)
    def wrapper(x):
        func(x)
        print('done inside wrapper')
    return wrapper

@somedec
def mini(x):
    print( x + 5)

mini(5)
print(mini.__name__)

# another view

def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(name):
            for i in range(n):
                func(name)#youHaveToReturn = func(name)
            # return youHaveToReturn

        return wrapper

    return decorator

@repeat(n=4)
def greet(name):
    print(f"Hello {name}")

greet('Juan')
print(greet.__name__)
# you can stacK decorators
# if you stack multiple decorators like:
"""
@b
@y
they will execute in the order they are placed
ao b first
then y
"""

# 3:30:15
# class decorators are pretty much the same
# look

class someclass:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self):
        self.count += 1
        print(f"It has been called {self.count} times")
        return self.func()

@someclass
def sayHi():
    print('Hi!')

sayHi()
sayHi()


# generators!!
'''
they are a way to generate iterables at command inside a class, thus, they are 
efficient
use the "yield" reserved word
'''

def mygenerator(): # you can have more than 1 yield
    yield 1
    yield 2

print(mygenerator())

for i in mygenerator():
    print(i)

# or

# x = mygenerator() 
# the generator behaves like obj, 
# so you call and assign to a var and the use the next function
# print(x)
x = mygenerator()
objHandler = next(x)
print(objHandler)
objHandler = next(x)
print(objHandler)
"""
an interesting behavior that the generators have is that when next is called
it stops at the first encounter of a yield,
and thus anything bellow the function definition 
will not be even lookekd at
"""
def lol(n):
    while n > 0:
        print("before yield")
        yield n
        print("after yield")
        n -= 1
y = lol(4)
print(next(y))
# print(next(y))

'''
# the generator can also be an argument
x = mygenerator()
print(sorted(x))
'''
# lufi = [1, 2, 3, 4, 5]
# lufi[0], lufi[2] = lufi[2], lufi[0]
# print(lufi)
# lufi[0] = lufi[2] 
# lufi[2] = lufi[0]
# print(lufi)

# generator expressions!!!

somegen = (i for i in range(10) if i % 2 == 0)
print(next(somegen))
print(next(somegen))
print(next(somegen))

# almost like list comprehensions, but more efficient