import math as m

print(' As quadratic equation : ax² + bx + c , enter value of \n')
a = float(input(' a = '))
b = float(input(' b = '))
c = float(input(' c = '))

print('Calculating....')
print('Sol : \n')
print('=> ',a,'x² + ' , b, 'x + ' , c)

D = m.pow(b,2) - 4*a*c

X = (-b - m.sqrt(D))/2*a*c
Y = (-b + m.sqrt(D))/2*a*c

if D < 0 :
	print('=> Roots of this solution is imaginary ..')
	print('=> This equation cannot solved further...')

elif D > 0 :
	print('=> This equation have real and unequal solutions...')
	print('=> alpha(X) = ',X)
	print('=> beta(Y) = ',Y)
elif D == 0 :
	print('=> This equation have real and equal solutions...')
	print('=> alpha(X) = ',X)
	print('=> beta(Y) = ',Y)
else:
	print('Invalid Input')