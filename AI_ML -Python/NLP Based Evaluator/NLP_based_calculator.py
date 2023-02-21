# NLP based calculator
import  math as m


while True :
	
	expression = input("\n enter expression > ").replace("add","+").replace("substract","-").replace("multiple","*").replace("divide","/").replace("plus","+").replace("minus","-").replace("multiplied by","*").replace("divided by","/")
	
	# calculating normal expressions
	if "+" in expression or "-" in expression or "*" in expression or "/" in expression :
		try:
			print(" result > ", eval(expression))
		except Exception as e :
			print(e)
			
	# calculating areas and perimeters
	# square
	elif "area" in expression and "of" in expression and "square" in expression :
		expression = expression.replace("area of square","")
		side = float(input("\n enter side > "))
		print(" area of square with side ",side,"=",pow(side,2))
	elif "perimeter" in expression and "of" in expression and "square" in expression :
		side = float(input("\n enter side > "))
		print(" perimeter of square with side ",side,"=",4*side)

	# rectangle
	elif "area" in expression and "of" in expression and "rectangle" in expression:
		length = float(input("\n enter length > "))
		width =  float(input(" enter width > "))
		print("area of rectangle with given dimensions  =  ",length*width)
	elif "perimeter" in expression and "of" in expression and "rectangle" in expression:
		length = float(input("\n enter length > "))
		width =  float(input(" enter width > "))
		print(" perimeter of rectangle with given dimensions  =  ", 2*(length+width))
		