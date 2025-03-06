import os
target = input("file dir: ")
list = list(os.walk("TESTDIR"))
print(list)
