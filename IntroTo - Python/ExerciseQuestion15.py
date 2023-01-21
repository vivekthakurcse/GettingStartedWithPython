# WAP to input cost price , selling price and print profit

cp = float(input(" Enter cost price = "))
sp = float(input(" Enter selling price = "))
if sp>cp:
	print(" Profit earned = " , (sp-cp) , "rs")
else :
	print(" Loss happened ")