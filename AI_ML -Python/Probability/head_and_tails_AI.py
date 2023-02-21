
n = int(input(" Enter No. of Coins  = "))
outcomes = pow(2,n)
print(" Number of outcomes = ", outcomes)

for i in range(n+1):
    num_tails = n - i
    probability = 1/outcomes
    print(" Probability of ", i, " heads and", num_tails, "tails = ", probability )

# Possibilities
for i in range(outcomes):
    
    outcome_str = bin(i)[2:]
    outcome_str = '0'*(n-len(outcome_str)) + outcome_str
    outcome_str = outcome_str.replace('0', ' T ').replace('1', ' H ')
    print(outcome_str)
    