#COUNTDOWN
for i in range(420,0, -1):
    print(i)

#PRINT AND RETURN
blackbook = [1, 2]
def blackfunct():
    for x in range(0,1):
        print (blackbook[0])
        return blackbook[1]
print(blackfunct())

#First Plus Length
def listfunct(list):
    add = list[0] + len(list)
    print(add)
print(listfunct([1,2,3]))

#Values Greater than second
list = [1,2,3,4]
def listfunct(list):
    listx = []
    for x in range(len(list)):
        if list[x] > list[1]:
            listx.append(list[x])
    print(listx)
print(listfunct([1,2,3,4]))

#This Length, That value

def listfunct(size, value):
    listx = []
    for x in range(0, size):
        listx.append(value)
    return listx
print(listfunct(4,5))

#Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.