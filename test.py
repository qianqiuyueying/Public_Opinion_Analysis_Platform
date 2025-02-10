from util.tool import *

password = "123456"
hashed_password = PasswordManager.hash_password(password)
print(PasswordManager.check_password(hashed_password, password))