import hashlib
hashed = hashlib.md5("password".encode()).hexdigest()
print(hashed)
print(len(hashed))
