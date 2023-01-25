# Type checking and error checking 
# Type Checking : checking the type of a variable is known as type checking . it can be done by type checking.
# eg :- 
var_1 = "Vivek"
print(type(var_1))
# Type Casting or Type Converstion : Converting One Variable into another type of data type
# print(type(int(var_1))) this is wrong because the string cannot be converted into int , float
# lets take an another example
length = len(var_1)
# print("The string has " + length + "characters") length cannot be conactinate because length is an integer
# correcr way
print("This string has " + str(length) + " characters") #by coberting length -> string
# checking the type of new length
new_len = str(length)
print("for new length type = ")
print(type(new_len))
# for old length
print("for previous length = ")
print(type(length))

#  taking to integer as string and concatinate
print("10"+"10")
print("sum after converstion = ")
print(int("10")+int("10"))

#  take to input and print sum
var_2 = input("Enter input var 2 = ")
var_3 = input("Enter input var_3 = ")
sum = int(var_2) + int(var_3)
print(sum)