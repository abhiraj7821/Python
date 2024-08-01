# sum of even numbers

n=int(input("Enter a number n: "))
sum=0
for i in range(1,n+1):
    if(i%2==0):
        sum+=i

print("Sum of even numbers in range Num is: ",sum)