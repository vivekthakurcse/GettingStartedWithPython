#Write a program to read today's date from user and displays how many days left in current month

date = int(input(" Enter date : "))
month = input(" Enter month (jan - dec ) :").lower()
year = int(input(" Year : "))

print(" Today's date : ", date ,"-", month , "-" , year)
if month == "jan"  or month =="march" or month=="may" or month =="july" or month == "aug" or month =="oct" or month=="dec":
	
	days_left = 31 - date
	print(" Days left in " , month , "of year" , year ," = " , days_left)
	
elif month == "feb" :
	
	check = year/4
	if(check==0):
		days_left = 29-date
		print(" Days left in " , month , "of year" , year ," = "  , days_left)
	else :
		days_left = 28-date
		print(" Days left in " , month , "of year" , year ," = "  , days_left)
		
else :
	days_left = 30-date
	print(" Days left in " , month , "of year" , year ," = " , days_left)