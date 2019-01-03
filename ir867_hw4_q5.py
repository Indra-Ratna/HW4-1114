#Indra Ratna
#CS-UY 1114
#09 Oct 2018
#Homework 4
#Problem 5
"""
x = int(input("Enter a positive integer: "))
u=x
num_ast = (2*x)-1
num_space = 0
while(u>0):
    print(" "*num_space+"*"*num_ast+" "*num_space)
    num_ast-=2
    num_space+=1
    u-=1
num_ast = 1
num_space-=1
while(u<x):
    print(" "*num_space+"*"*num_ast+" "*num_space)
    num_ast+=2
    num_space-=1
    u+=1

"""
x = int(input("Enter a positive integer: "))
u=x
num_space = ((2*x)-1)//2
num_ast = 1
while(u>0):
    print(" "*num_space+"*"*num_ast+" "*num_space)
    num_ast+=2
    num_space-=1
    u-=1

