#pylint:disable=E0001
#pylint:disable=E0001
#pylint:disable=E0001
#pylint:disable=E0001
#pylint:disable=E0001

n = input("Position[n] of input : ")
n = input("Position[m] of input : ")
turn[n][m] = "O"
num1 = "X"


print("\n    " + "1" + "2"  + "3" )
print("\n 1   " + num1 + " | "  + num2 , turn[n][m]  + " | " +   num3 , turn[n][m])
print("      ___________")
print("\n 2   " + num4,turn[n][m] + " | "  + num5,turn[n][m]  + " | " +   num6 , turn[n][m]   )
print("      ___________")
print("\n 3   " + num7,turn[n][m] + " | "  + num8 , turn[n][m] + " | " +   num9 , turn[n][m]   )

while True :
	if turn[1][2] == 'O' :
	   	num4 = "X"
    elif turn[3][1] == 'O' :
     	num5 = "X" 
    elif turn[3][3] == 'O' :
    	num8 = "X"
    else :
    	print("Nothing")