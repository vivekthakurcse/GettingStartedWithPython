#  Project 1 : - Make a command line caluclator
print("------------------ Clac Me -----------------")
print("\n  1 for Add (+)                  2 for Sub (-)  ")
print("  3 for Multiplication(*)        4 for divide (/)")


while True :
    
    print("\n ---------------------------------------")
    choice =  int(input("Enter your choice (1-4) = ")) 
    
    if choice > 4 :
        print("-__- enter a correct choice between 1-4")
        
    else :
        var_1 = float(input("Enter First Number = "))
        var_2 = float(input("Enter Second Number = "))
        if choice == 1:
            sum = var_1 + var_2
            print("Sum of numbers " + str(var_1) + " and " + str(var_2) + " = ",sum)
        elif choice == 2 :
            sub = var_1 - var_2
            print("Difference of numbers " + str(var_1) + " and " + str(var_2) + " = ",sub)
        elif choice == 3 :
            product = var_1*var_2
            print("Product of numbers " + str(var_1) + " and " + str(var_2) + " = ",product)
        elif choice == 3 :
            div = var_1*var_2
            print("On division of numbers " + str(var_1) + " and " + str(var_2) + "result = ",div)