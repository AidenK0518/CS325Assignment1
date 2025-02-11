import time

def timer(func):
    def wrapper(*arg):
        t = time.time()
        res = func(*arg)
        print ("Colltaz took ")
        print (time.time()-t)
        return res
    return wrapper

@timer
def collatz(n):
    checkcase = n % 2
    if checkcase == 0:
        print(n)
        return collatz(n/2)
    elif n == 1:
        print(n)
        return 1
    else:
        print(n)
        return collatz((3*n)+1)
    
collatz(275426237)