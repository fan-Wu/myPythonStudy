import time

def deco(func):
    def temp():
        t1=time.time()
        func()
        t2=time.time()
        dt=(t2-t1)*1000
        print(dt)
    return temp

@deco
def myfun():
    print('start')
    time.sleep(1)
    print('end')

myfun()

