while True:
	
	Arthimetic = input("What do you want to do? ")
	
	if Arthimetic == "area of circle":
		val_1 = input("Radius of circle: ")
		
	if Arthimetic == "area of sector":
		val_1 = input("Tetha: ")
		val_2 = input("radius: ")
		
	if Arthimetic == "area of major sector":
		val_1 = input("Tetha: ")
		val_2 = input("radius: ")
		
	if Arthimetic == "length of an arc":
		val_1 = input("Tetha: ")
		val_2 = input("radius: ")
		
	if Arthimetic == "area of square":
		val_1 = input("Side of square: ") 
		
	if Arthimetic == "area of rectangle":
		val_1 = input("Length: ")		
		val_2 = input("Breadth: ")
		
	if Arthimetic == "volume of cube":
		val_1 = input("Side: ")
		
	if Arthimetic == "volume of cuboid":
		val_1 = input("Length: ")
		val_2 = input("Breadth: ")
		val_3 = input("Height ")
		
	if Arthimetic == "T.S.A of cuboid":
		val_1 = input("Length: ")
		val_2 = input("Breadth: ")
		val_3 = input("Height: ")
		
	if Arthimetic == "T.S.A of cube":
		val_1 = input("Side: ")
		
	if Arthimetic == "√":
		val_1 = input("Number: ")
		
	if Arthimetic == "+":
		val_1 = input("Please enter your number here ")
		val_2 = input("Please enter your 2nd Number here ")
			
	if Arthimetic == "-":
		val_1 = input("Please enter your number here ")
		val_2 = input("Please enter your 2nd Number here ")
			
	if Arthimetic == "*":
		val_1 = input("Please enter your number here ")
		val_2 = input("Please enter your 2nd Number here ")
			
	if Arthimetic == "/":
		val_1 = input("Please enter your number here ")
		val_2 = input("Please enter your 2nd Number here ")
		
	if Arthimetic == "%":
		val_1 = input("Please enter your number here ")
		val_2 = input("Please enter your 2nd Number here ")
			
	else:
		Result = "Invalid Input"
		
	if Arthimetic == "+":
		Result = float(val_1) + float(val_2)
		
	if Arthimetic == "-":
		Result = float(val_1) - float(val_2)
		
	if Arthimetic == "*":
		Result = float(val_1) * float(val_2)
		
	if Arthimetic == "/":
		Result = float(val_1) / float(val_2)
		
	if Arthimetic == "%":
		Result = float(val_1) / float(val_2) * 100
		
	if Arthimetic == "√":
		Result = float(val_1) ** 0.5
		
	if Arthimetic == "area of circle":
		Result = 22/7 * float(val_1) * float(val_1)
		
	if Arthimetic == "area of square":
		Result = float(val_1) * float(val_1)
		
	if Arthimetic == "area of rectangle":
		Result = float(val_1) * float(val_2)
		
	if Arthimetic == "volume of cube":
		Result = float(val_1) * float(val_1) * float(val_1)
		
	if Arthimetic == "volume of cuboid":
		Result = float(val_1) * float(val_2) * float(val_3)
		
	if Arthimetic == "T.S.A of cuboid":
		Result = 2 * ( float(val_1) * float(val_2) + float(val_2) * float(val_3) + float(val_3) * float(val_1))
		
	if Arthimetic == "T.S.A of cube":
		Result = 6 * float(val_1) * float(val_1)
		
	if Arthimetic == "area of sector":
		Result = float(val_1) / 360 * 22/7 * float(val_2) * float(val_2)
	
	if Arthimetic == "area of major sector":
		Result = 360 - float(val_1) / 360 * 22/7 * float(val_2) * float(val_2)
		
	if Arthimetic == "length of an arc":
		Result = float(val_1) / 360 * 2 * 22/7 * float(val_2)
		
	if Result == "Invalid Input":
		print ("Invalid")
		
	else:
		print ("Your Answer" , Result)
		