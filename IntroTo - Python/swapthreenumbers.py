# WAP to input three numbers and swap them

num1 = int(input(" Enter first number  = "))
num2 = int(input(" Enter second number = "))
num3 = int(input(" Enter third number = "))

print(" Numbers before swaping : ")
print(" Num1 = " , num1 , " Num2 = " , num2 , " Num3 = " , num3)

#temp = num1
#temp2 = num2
#num1 = num3
#num2 = temp2
#num3 = temp

num1 , num2 , num3 = num3, num1 , num2
print(" Numbers after swaping : ")
print(" Num1 = " , num1 , " Num2 = " , num2 , " Num3 = ", num3)