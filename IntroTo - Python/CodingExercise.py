# Q.1 two numbers
a = int(input("enter a = "))
b = int(input("enter b = "))

# logic 1
temp = a # storing value of a into temprorary varriable
a = b 
b = temp
print("After swapping  by method 1 : " + "\n a = " , a , "\n b = " , b)

# logic 2
a , b = a, b
print("After swapping  by method 2 : " + "\n a = " , a , "\n b = " , b)

# --------------- Variable Naming Rules -------------------------
# 
# 1.) It is recommended to take a meaningful name for the variable
# 2.) Variable names can only contain letters, numbers A-Z and 0-9
#  example : name2, name3, name4
# 3.) Spaces between names is not allowed
# 4.) Special symbols are not allowed
# 5.) Variable names can only starts with a letter or an underscore
# 6.) Reserveds words are not allowed
# 7.) Python is case-sensitive
# 
#  if your variable obeys the following rules you are ready to go
# 
# --------------------- Naming Conventions ----------------------
# 
# Pascal naming conventions used classes -  class ClassName : 
# camelCase naming convention used for functions - def functionName()::
# snakeCase naming convention used for variables - var_A = int(input("var_A = "))
