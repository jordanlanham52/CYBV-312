def square(x):

    answer = x * x 

    return answer 

n = 5

result = square(n)

print(result, n)

def addEm(x, y, z):
    return x+y+z
    print('the answer is', x+y+z)

def addEm(x, y, z):
    print(x+y+z)

s = "python rocks"
for idx in range(len(s)):
   if idx % 2 == 0:
      print(s[idx])

#s = "Ball"
#s[0] = "C"
#print(s)

s = "ball"
r = ""
for item in s:
   r = item.upper() + r
print(r)

def f1(x):
    for counter in range(x):
        runningtotal = 0
        runningtotal = runningtotal + x
    return runningtotal

def f2(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x

    return runningtotal

toSquare = 10
f1Result = f1(toSquare)
f2Result = f2(toSquare)
print(f1Result, f2Result)

def removeSomeChars(s):
    vowels = "aeiouAEIOU"
    digits = "0123456789"
    newS = ""
    for eachChar in s:
        if (eachChar not in vowels) and (eachChar not in digits):
            newS = newS + eachChar
    return newS

print(removeSomeChars("CYBV312"))

# nested if-else statement

x = -10

if x < 0:

    print("The negative number ",  x, " is not valid here.")

else:

    if x > 0:

        print(x, " is a positive number")

    else:

        print(x, " is 0")

x = -10

if x < 0:

    print("The negative number ",  x, " is not valid here.")

elif x > 0:

    print(x, " is a positive number")

else:

    print(x, " is 0")

x = -10

if x < 0:

    print("The negative number ",  x, " is not valid here.")

if x > 0:

    print(x, " is a positive number")

else:

    print(x, " is 0")

sum = 0

for k in range(1, 22, 3):

    sum = sum + k

print(sum)

sum = 0

k = 1

while k < 22:

    sum = sum + k

    k = k + 3

print(sum)

sum = 0

k = 1

def printnums(x,y):

    for h in range(y):

        print("We made it here!")

        for i in range(x):

            print("We made it here!")

printnums(5, 3)