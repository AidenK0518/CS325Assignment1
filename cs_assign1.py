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
def defcollatz(n):
    checkcase = n % 2
    if checkcase == 0: #Check if Even
        print(n)
        return collatz(n/2)
    elif n == 1: #Check if Done
        print(n)
        return 1
    else: #Number has to be an odd number that is not 1
        print(n)
        return collatz((3*n)+1)
    
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
    
defcollatz(275426237)