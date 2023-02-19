
# Implementation of Rock , Paper , Scizor AI
import random


print("\n\n ------------------- Game Starts Now ---------------------")
# 0 for Rock
# 1 for Paper
# 2 for Scizor
print("\n\t\t\t Rock    → 0")
print("\n\t\t\t Paper   → 1")
print("\n\t\t\t Scizor  → 2")


for i in range(3) :
	print("\nRound " + str(i+1))
	print("-----------------------")
	userInput = int(input("\n      Enter 0 for Rock , 1 for Paper and 2 for Scizor :  "))
	#Checking if the user inputs a Valid number
	if userInput > 2 :
		print("\n\tPlease enter a valid input = _ =  ")
	else :
		if userInput == 0 :
		  	print("\n\t You : Rock")
		elif userInput == 1 :
		  	print("\n\t You : Paper")
		else :
		  	print("\n\t You Scizor")
		 
		#generating a computer response
		Response = random.randint(0,2)
		if   Response == 0 :
		  	print("\n\t Me : Rock")
		elif Response == 1 :
		  	print("\n\t Me : Paper")
		else :
		  	print("\n\t Me : Scizor")

		#Playing with player
		if userInput == Response :
			  print("\n\t\t Match Draw : [")
		elif userInput == 0 and Response == 2 or userInput == 1 and Response == 0 or userInput == 2 and Response == 1 :
			 print("\n\t\t Congratulations you win ^⁠_⁠^")
		else :
			print("\n\t\t Hehehehe ... I win <⁠(⁠￣⁠︶⁠￣⁠)⁠> ")
			