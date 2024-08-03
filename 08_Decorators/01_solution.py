#DECORATORS
#Problem: Write a decorator that measures the time a function takes to execute.

import time

def timer (func):
    def wrapper(*arrgs,**kwargs):
        start=time.time()
        result=func(*arrgs,**kwargs)
        end=time.time()
        print(f"{func.__name__} run in {end-start} time")
        return result
    return wrapper

@timer
def example_function(n):
    print("Hi")

example_function(5)