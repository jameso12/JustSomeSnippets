# Multiporcessing
from multiprocessing import Process, Value, Array, Lock, Queue, Pool
import os
import time

def cube(number):
    return number * number * number


if __name__ == "__main__":
    numbers = range(10)

    pool = Pool()

    # map, apply, join, close
    result = pool.map(cube, numbers)
    pool.close()
    pool.join()

    print(result)