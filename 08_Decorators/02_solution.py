#Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.


def funcName(func):
    def wrapper(*args):
        args_value=args
        func(*args)
        print(f"Func name: {func.__name__} and argument {args_value}")
    return wrapper

@funcName
def expample(n):
    print("input",n)

expample(5)

