#Jordan Lanham Assignment 1 1/23/24
#Variable Declaration

#imports randint function from the random library
from random import randint

#Declaring variables
firstName = "Jordan"
lastName = "Lanham"
title = "beetlejuice"
title = title.upper() #adjusts the title variable into all capitals
quote = "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma — which is living with the results of other people's thinking."
author = " Steve Jobs "

#Print introduction
print("Hello my name is ",firstName," ",lastName)

#Random number generator and even odd checker
for i in range(7):
    aKey = randint(1,6)
    if aKey % 2 != 0:
        print(quote, author)
    else:
        print(title.title(), title.lower())
print("Done!")