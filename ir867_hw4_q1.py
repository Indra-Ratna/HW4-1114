#Indra Ratna
#CS-UY 1114
#09 Oct 2018
#Homework 4

i=0
j=0
while i<5:
    i+=1
    j+=i
    print(j*"@")
for x in range(0,5):
    for y in range(x, 0, -1):
        print(x, y)
foo = ""
x = 0
while x < 10:
    foo += str(x)
    x += 3
print(foo)

"""
Number 1 prints
@
@@
@@@
@@@@

Number 2 prints
0 0
1 0
2 1 0
3 2 1 0
4 3 2 1 0
5 4 3 2 1 0

Number 3 prints
0369
"""







