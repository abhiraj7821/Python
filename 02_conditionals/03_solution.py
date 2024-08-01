score=int(input("Enter your score"))
grade='A'
if(score<60):
    grade='F'
elif(score<70):
    grade='D'
elif(score<80):
    grade='C'
elif(score<90):
    grade='B'
else:
    grade='A'

print("Your grade is: ",grade)