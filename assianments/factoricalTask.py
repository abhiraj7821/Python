
num=int(input("ENTER THE NUMBER: "))

def findFac(num):
    if num==1 or num==0:
        return 1
    
    return num*findFac(num-1)
    
