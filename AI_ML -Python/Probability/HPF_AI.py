# Implement of a program that can find the probability
# of a getting a head or a tail if the coin is flipped
n = int(input(" Enter No. of Coins  = "))
outcomes = pow(2,n)
print(" Number of outcomes = ", outcomes)

# Tying to print out the outcomes
#i = 1
#	for  p in range(n):
#			q = p - 2
#			print(" H "*(p-q) +" T "*q)
#for m in range(outcomes):
#	for i in range(n):
#		for p in range(m):
#			print( " H "*(p-i)+ " T "*((m-i)-p))

print()

for i in range(n+1):
    num_tails = n - i
    probability = 1/outcomes
    print(" Probability of ", i, " heads and", num_tails, "tails = ", probability )
    
    
print()


# Possibilities
for i in range(outcomes):
    
    outcome_str = bin(i)[2:]
    outcome_str = '0'*(n-len(outcome_str)) + outcome_str
    outcome_str = outcome_str.replace('0', ' T ').replace('1', ' H ')
    print(outcome_str)
    
