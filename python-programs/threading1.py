from threading import Thread
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello!")
            sleep(1)
        print("------------------------------")



class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi!")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()


t1.join()
t2.join()  #if not using this, then it will print them before
print("Bye") #main thread prints this

# main thread- default thread

# cretaing multiple thread
