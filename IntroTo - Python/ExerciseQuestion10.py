# WAP to find the area of a triangle
import math as m

a = int(input(" Enter side a = "))
b = int(input(" Enter side b = "))
c = int(input(" Enter side c = "))

s = (a + b + c)/2
area = m.sqrt(s*((s-a)*(s-b)*(s-c)))
print(" Area of given triangle with sides : " , a , b , c , " = " , area, "unit²")