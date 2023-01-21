# WAP to enter a input value in tonnes and convert it into quintals and kilograms
# 1 tonne  = 10 quintals
# 1 tonne = 1000kgs
# 1 quintal = 100kg

tonnes = float(input(" Enter value in tonnes : "))
quintals = tonnes*10
kilograms = tonnes*1000

print(tonnes , "Tonnes  = " , quintals , "quintals")
print(tonnes , "Tonnes = " , kilograms , "kilograms")