# WAP that accepts marks in five subjects and outputs average marks

print(" Enter your marks in following subjects : ")
mark1 = float(input(" Maths =  "))
mark2 = float(input(" Science = "))
mark3 = float(input(" Social Science = "))
mark4 = float(input(" Hindi = "))
mark5 = float(input(" English = "))

if mark1 <= 100 and mark2 <=100 and mark3<=100 and mark4 <=100 and mark5 <= 100 :
	average = (mark1+mark2+mark3+mark4+mark5)/5
	print(" Your average marks is "  , average)

else :
	print("        Please enter your marks correctly ")