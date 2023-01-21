# WAP to input a number and find its five multiples

a = int(input(" Enter a number = "))
i = 1
print(" First five multiples of " , a , " are :")
for i in range(6):
	print(" " , a*i)