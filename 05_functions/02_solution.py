#Problem: Create a function that takes two numbers as parameters and returns their sum.

def calculateSum(num1,num2):
    return (num1+num2)

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))

print("Sum of above two number is:",calculateSum(num1,num2))