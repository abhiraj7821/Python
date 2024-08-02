#Create a function that returns both the area and circumference of a circle given its radius.

def calculation(rad):
    circumfarence=2*3.15*rad
    area=3.14*(rad**2)
    return[circumfarence,area]

rad=int(input("Enter Radius:"))

sol=calculation(rad)
print("Circumfarence of circle:",sol[0])
print("Area of circle:",sol[1])