# NLP based calculator
import  math as m


while True :
	
	print("\n enter expression ")
	expression = input(" > ").replace("add","+").replace("substract","-").replace("multiple","*").replace("divide","/").replace("plus","+").replace("minus","-").replace("multiplied by","*").replace("divided by","/")
	# calculating normal expressions
	if "+" in expression or "-" in expression or "*" in expression or "/" in expression :
		try:
			print(" result > ", eval(expression))
		except Exception as e :
			print(e)
			
	# 2D figures

	# square
	elif "area" in expression and "of" in expression and "square" in expression :
		expression = expression.replace("area of square","")
		side = float(input("\n enter side = "))
		print(" area of square with side ",side,"=",pow(side,2))
	elif "perimeter" in expression and "of" in expression and "square" in expression :
		side = float(input("\n enter side = "))
		print(" perimeter of square with side ",side,"=",4*side)

	# rectangle
	elif "area" in expression and "of" in expression and "rectangle" in expression:
		length = float(input("\n enter length = "))
		width =  float(input(" enter width = "))
		print("area of rectangle with given dimensions  =  ",length*width)
	elif "perimeter" in expression and "of" in expression and "rectangle" in expression:
		length = float(input("\n enter length = "))
		width =  float(input(" enter width = "))
		print(" perimeter of rectangle with given dimensions  =  ", 2*(length+width))
	
	# triangle
	elif "area" in expression and "of" in expression and "triangle" in expression:
		radius = float(input("\n radius = "))
		area = (3.14)*(radius*radius)
		print(" area of circle = ",area)
	elif "circumference" in expression and "of" and "circle" in expression:
		radius = float(input("\n radius = "))
		cir_f = 2*(3.14)*radius
		print(" circumference of circle = ",cir_f)
		
	# sector
	elif "area" in expression and "of" in expression and "sector" in expression:
		thetha = float(input("\n angle ⁰ = "))
		radius = float(input(" radius of sector \ length of arm = "))
		area = (thetha/360)*(3.14)*(radius*radius)
		print(" area of given sector = " , area)
	elif "perimeter" in expression and "of" in expression and "sector" in expression:
		thetha = float(input("\n angle ⁰ = "))
		radius = float(input(" radius of sector \ length of arm = "))
		perimeter = (thetha/360)*(3.14)*(2*radius) + 2*radius
		print(" area of given sector = " , area)
	
	# 3D figures 