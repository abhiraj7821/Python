#Check if a number is prime

num=7
is_prime=True

if(num>1):
    for i in range(2,num):
        if(num%i)==0:
            is_prime=False

print(is_prime)