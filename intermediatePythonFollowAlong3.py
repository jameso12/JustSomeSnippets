# Threding vs Multiprocessing
# Multiprossesing

"""
 processes can spawn threads
 process are interuptable
 do not have gil limitations

 threads can not be interrupted
 cannot be run on parrallel
 have gil limitation 
 """
'''
from multiprocessing import Process
import os

def squareNUm():
    for i in range(100):
        i*i

processes = list()
num_processes = os.cpu_count()

# create porcesses
for i in range(num_processes):
    p = Process(target=squareNUm)
    processes.append(p)

#start
for p in processes:
    p.start()
#join
for p in processes:
    p.join()
'''
# MultiThreading

'''
from threading import Thread
import os

def squareNUm():
    for i in range(100):
        i*i

threads = list()
num_threads = os.cpu_count() # since threads are not really cpu bound you may place something like 10

# create porcesses
for i in range(num_threads):
    p = Thread(target=squareNUm)
    threads.append(p)

#start
for p in threads:
    p.start()
#join
for p in threads:
    p.join()
'''
import functools

def some(n):
    def decor(func):
        @functools.wraps(func)
        def wrapper(name):
            x = 0
            for i in range(n):
                func(name)
                x += 1
                print('iter', x)
        return wrapper
    return decor
        

@some(4)
def pn(name):
    print('Hello', name)

pn('James')
print(type(pn))
print(pn.__name__)