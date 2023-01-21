# WAP to calculate BMI (Body Mass Index ) of a person
# Body Mass is simple calculation using a person's height and weight
# The formula is a BMI = kg/m² simple calculation using person weight in kilograms
# and m² is their height in metres squared.

weight = float(input(" Enter your weight (in kilograms) = "))
height = float(input(" Enter your height ( in metres)   = "))

BMI =  weight/(height*height)

print(" Your BMI is : " , BMI)