# Relational Operator or Assignment Operator is used to  assigned values to a variable
# a = 5 but not 5 = a
# in mathematic a = 5 is equal to 5 = a but in programming  left hand size must be a variables
# Relational Operators:- 
#                   Assignment Operators : - ' = '
#                   Short-Hand Assignment Operator :- +=  
#                                                     -= 
#                                                     *=    
#                                                     /= 
#                                                     %=
#  eg :- 

a = 5
print('a = ', a) 
# a += ?
a += a
print('a += ', a) # a += a+a = 5+5 = 10
a -= a
print('a -= ', a) # a -= a-a = 10-10 = 0
a *= a
print('a *= ', a) # a *= a*a = 0*0 = 0
# a /= a
# print('a /= ', a)  a /= a/a = 0/0 = not defined
# a %= a
# print('a %= ', a) 

#  Comparison operator :- the operator which is use to compare two values is known as comparison operator.
# < , > ,<= ,=>,==
print('------------------------------------------------')
b = 5
if b > 4 :
    print('yes')
else :
    print('no')
    
if b < 4 :
    print('yes')
else :
    print('no')
    
if b >= 4 :
    print('yes')
else :
    print('no')
    
if b <= 4 :
    print('yes')
else :
    print('no')
    
if b == 4 :
    print('yes')
else :
    print('no')