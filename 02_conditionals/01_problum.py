age= input("Enter Your Age: ")

age_in_int=int(age)

age=age_in_int

if age<13:
    print("Child")
elif age<20:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Senior")
