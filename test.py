from util.tool import *

password = "123456"
hashed_password = PasswordManager.hash_password(password)
print(hashed_password)