#Indra Ratna
#CS-UY 1114
#09 Oct 2018
#Homework 4
#Problem 7

x =int(input("Enter a binary number: "))
c=x
decimal = 0
i = 0
n = 0
while(c!=0):
    dec = c%10
    decimal = decimal +(dec*(2**i))
    c=c//10
    i+=1
print(decimal)
