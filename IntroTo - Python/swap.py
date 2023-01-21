# WAP to input two numbers and swap it

num1 = int(input(" Enter first number : "))
num2 = int(input(" Enter second number : "))

print(" Numbers before swaping : ")
print(" Num1 = ", num1 , "Num2 = " , num2)

temp = num2
num2 = num1
num1 = temp
print(" Numbers after swaping : ")
print(" Num1 = " , num1 , "Num2 = " , num2)