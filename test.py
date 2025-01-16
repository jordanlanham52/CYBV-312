import hashlib

hash = hashlib.sha256(b"hello world").hexdigest()

print(hash)

