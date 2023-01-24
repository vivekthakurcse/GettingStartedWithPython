# ----------------------------- Data types in python ------------------------
# 
# There are two types of data types in python :
#  1.) Premitive Data Types 
#  2.) Non-Premitive Data Types
# 
# As Python is an object oriented programming language so everything is considerd as classes. 
# So every data types is considered as class and the variables you declare is considred as object of these classes.

var_1 = 3 # the data type of this variables is int

# How to check data type of a variable
print(type(var_1))

# how to intilized data types while taking an input
# python takes every input as string by default so if want to take an integer value we have to use int() function
var_2 = int(input("integer type var_2 = "))
var_3 = float(input("floating point var_3 = "))
var_4 = str(input("string type var_4 : "))

# -------------------------------------------------

print("var_2 = " , var_2, type(var_2))
print("var_3 = " , var_3, type(var_3))
print("var_4 = " , var_4, type(var_4))