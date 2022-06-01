from operator import imod
from threading import Thread
from time import sleep

def func1():
    for i in range(500):
        print('worker 1')

def func2():
    for i in range(500):
        print("worker 2")




class A:
    def print_hello(self):
        for i in range(5):
            print("Hello")
            sleep(1)
        
    def print_hi(self):
        for i in range(5):
            print("Hi")
            sleep(1)


o = A()

t1 = Thread(target=o.print_hello)
t2 = Thread(target=o.print_hi)

t1.start()
t2.start()
t1.join()
t2.join()
print("END")
