#Problem: Given a string, find the first non-repeated character.

input_str="teetraba"

for char in input_str:
    
    if(input_str.count(char)==1):
        print("First non-repeated character is:",char)
        break