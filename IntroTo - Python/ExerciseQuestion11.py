# WAP to  compute simple intrest and compound interest
# simple interest = p*r*t/100
# compound interest = p*(1+r/n)^nt

print("Note :  If you Only want SI then fill number of times applied 0")
principal = float(input("\n Enter Principal = "))
rate = float(input(" Enter Rate = "))
time = float(input(" Enter time period = "))
n = int(input(" Enter no. of times applied = "))


si = (principal*rate*time)/100
print("\n\n Simple Interest = " , si)


if n == 0 :
	print(" Compound Interest = none")
else :
	ci = principal*(pow((1+rate/n),(n*time)))
	print(" Compound Interest = ", ci)