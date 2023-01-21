# WAP that accepts your height in centimetres and convert it to feets and inches

height = float(input(" Enter your height (in cm) = "))

inches = height/2.54
foot = inches/12

print(" Your height is equals to " , foot ,"feets" , "\n or " , inches , "inches")