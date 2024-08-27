
# Reading a file 
# file1=open("data.txt","r")

# contents=file1.read()

# print(contents)
# file1.close()

#  Working using with block

# with open("data.txt","r") as file1:
#     for line in file1:
#         print(line.strip())


#writing to a file

# file1=open("data.txt","w")

# file1.write("Abhishek, 101, A+\n")

# file1.close()

# str="Abhishek, 101, A+"
# str=str.replace(",","")
# print(str)

with open("data.txt","r") as file1:
    print("BEFOR:")
    for line in file1:
        print(line)
    
    print("AFTER:")
    for line in file1:
        print(line)

    # for line in file1:
    #     line=line.replace(",","")

   

    


