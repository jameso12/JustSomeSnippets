# Multithreading
# threads live in the same memory space and thus sharing data is easy
from threading import Thread, Lock, current_thread
from queue import Queue # good for miltithread data exange and multiprocess data exange
# queue methods
# get() >> pops and returns first value
# put(arg) >> adds element ot list
# join() blocks until it is processed
# task_done() lets know that it has been prossesed

import time
# Lock is impirted to avoid race condition
# which is when 2 threads use same variable at same time, whih is no good

database_value = 0 

def increase(lock):
    global database_value

    lock.acquire() # locks so that one thread access it or "with lock:" and indent anddelete lock.release()
    local_copy = database_value

    # processing or just any process
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy

    lock.release() # releases the lock so that it can be used again

def worker(q, lock):
    while True:
        value = q.get()
        # process
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    num_therads = 10
    
    for i in range(num_therads):
        thread = Thread(target= worker, args= (q, lock))
        thread.daemon = True # default false, dies when the main thread dies
        thread.start()


    for i in range(1,21):
        q.put(i)

    q.join()

    print('end main')
