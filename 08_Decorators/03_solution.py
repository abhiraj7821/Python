#Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
import time


def cache(func):
    chace_value={}
    print(chace_value)
    def wrapper(*args):
        if(args in chace_value):
            return chace_value[args]
        result=func(*args)
        chace_value[args]=result
        return result
    return wrapper

@cache
def long_running_func(a,b):
    time.sleep(5)
    return a+b
    
print(long_running_func(2,3))
print(long_running_func(2,3))