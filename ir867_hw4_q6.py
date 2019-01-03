#Indra Ratna
#CS-UY 1114
#09 Oct 2018
#Homework 4
#Problem 6
import random
cpu = random.randint(1,100)
print("I'm thinking of a number betwen 1 and 100, try to guess it.")
x = (input("Please enter a  number between 1 and 100."))
if(not x.isdigit()):
    print('Sorry, but "'+ str(x)+'" is not a number between 1 and 100')
    x = (input("Please enter a  number between 1 and 100."))
elif(int(x)<0 or int(x)>100):
    print('Sorry, but "'+ str(x)+'" is not a number between 1 and 100')
    x = (input("Please enter a  number between 1 and 100."))
x=int(x)
guess = False
while(not guess):    
    if(x==cpu):
        print("Congratulations, you guessed the number!")
        guess = True
    elif(x<cpu):
        print("Sorry, your guess was too low, try again.")
        x = int(input("Please enter a  number between 1 and 100."))
    elif(x>cpu):
        print("Sorry, you guess was too high, try again.")
        x = int(input("Please enter a  number between 1 and 100."))
