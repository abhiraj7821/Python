# day="Wednesday"
# age=21

day=input("Enter day: ")
age=int(input("Enter your age: "))

price=12 if age>=18 else 8

if day=="Wednesday":
    price-=2

print("Your movie ticket price is $",price)