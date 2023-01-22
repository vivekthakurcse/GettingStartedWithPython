# input() is use to accept input from user
# example : input(prompt)
name = input("Enter your name : ")
print(name)

# input without prompt
print("What is your name?")
myname = input()
print("hello"+ myname)

# input() takes every input as a string so if we want to take a integer input or float you have to convert it by int() , float()...
num1 = int(input("Enter a integer : "))
num2 = float(input("Enter a float : "))
print("Integer variable = ", num1)
print("Float variable =" , num2)

# nested input() function
print("hello " + "..." + input("what is your name : "))