#Indra Ratna
#CS-UY 1114
#09 Oct 2018
#Homework 4
#Problem 4
import turtle

size = int(input("Enter number of sides: "))
length = int(input("Enter length: "))
angle = 360/size
i =0
if(size>=3):
    while(i<=size):
        turtle.forward(length)
        turtle.left(angle)
        i+=1
else:
    print("Not a valid number of sides for a polygon")
