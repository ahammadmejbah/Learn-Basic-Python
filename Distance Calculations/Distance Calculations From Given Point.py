"""Deep Neuron AI"""

import math

def distance(x1,y1,x2,y2):
    distance = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
    return distance

x1=int(input("Enter x1 : "))
y1=int(input("Enter y1 : "))
x2=int(input("Enter x2 : "))
y2=int(input("Enter y2 : "))

print("Distance between points : ", round(distance(x1,y1,x2,y2),2))