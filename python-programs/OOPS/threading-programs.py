from threading import Thread
from time import sleep
class A(Thread):
    def run(self):
        for i in range(4):
            print("Hello")
            sleep(1)
    

class B(Thread):
    def run(self):
        for i in range(4):
            print("Hi")
            sleep(1)
a = A()
b = B()

a.start()
b.start()

a.join()
b.join()

print("END")