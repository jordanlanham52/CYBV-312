import hashlib
import random

hash = hashlib.sha256(b"hello world").hexdigest()

print(hash)

num = random.randint(1,10)

print(num)




