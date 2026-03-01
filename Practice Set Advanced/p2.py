from time import time
def timer(func):
    def wrapper(n):
        t1=time() #initial time
        func(n)
        t2=time() #time taken
        print(t2-t1)
    return wrapper
@timer
def sum_n(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total

a=sum_n(1000000)

