# WAP that accepts cost of goods sold revenue generated , operating cost
# and Gross profit  ,net profit and net profit percentage


cgos = int(input('Enter cost of goods sold : '))
rg = int(input('Enter revenue generated : '))
oc = int(input('Enter operating cost : '))
gp = rg - cgos
np = gp - oc 
npp = np/rg*100 
print('Gross profit is', gp)
print('Net profit is', np)
print('Net profit percentage is', npp)