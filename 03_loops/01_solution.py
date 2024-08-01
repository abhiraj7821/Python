# counting all positive numbers

list= [1,2,3,-1,-2,-3,4,5,6,7,5]

positive_num_count=0

for num in list:
    if(num>0):
        positive_num_count+=1
print("Positive number count =",positive_num_count)