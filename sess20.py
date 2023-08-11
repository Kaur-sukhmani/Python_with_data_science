# Encrypting data
# hello -> encrypt() -> 123sdefe45666
import hashlib
password = input("Enter the password")
# Encode password to UTF-8
password = password.encode('utf-8')
password = hashlib.sha256(password).hexdigest() # universal traformation format
# hexdigest is the method
# sha256 s strong  secure hasg 256 bit encrytion
print(password)