# Factorial of a num using recursion

def factorial(num):
    if(num==1):
        return 1
    sol=num*factorial(num-1)
    return sol

num=int(input("Enter a num:"))

print("Factorial of num is:",factorial(num))