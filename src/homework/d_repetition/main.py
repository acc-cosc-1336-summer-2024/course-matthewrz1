#Homework 4 main code with menu

import repetition

def menu():

    print("Homework 4 menu, please choose an option below")
    print("1-Factorial")
    print("2-Sum odd numbers")
    print("3-Exit")

    selection = int(input("Please choose a menu item above: "))
    num = 0
    x = True
    Ask_Exit = "N"

    if selection == 1:

        num = int(input("You have chosen factorial, input a number between 0 and 10: "))

        while x == True:
            if num > 0 and num < 10:
                print("factorial of", num, "is: ", repetition.get_factorial(num))
                Ask_Exit = input("Would you like to exit? Y or N: ")
                if Ask_Exit == "Y":
                    print("You have exit the menu")
                    exit()
                elif Ask_Exit == "N":
                    print("Staying in factorial menu option")
                    num = int(input("Input a number between 0 and 10: "))
            elif num <= 0 or num >= 10:
                num = int(input("number not within 0 and 10, input a number: "))
    
    elif selection == 2:
        num = int(input("You have chosen sum of odd numbers, Input a number between 0 and 100: "))

        while x == True:
            if num > 0 and num < 100:
                print("sum of odd numbers of", num, "is: ",repetition.sum_odd_numbers(num))
                Ask_Exit = input("Would you like to exit? Y or N: ")
                if Ask_Exit == "Y":
                    print("You have exit the menu")
                    exit()
                elif Ask_Exit == "N":
                    print("Staying sum of odd numbers menu option")
                    num = int(input("Input a number between 0 and 100: "))
            elif num <= 0 or num >= 100:
                num = int(input("Number not within 0 and 100, input a number: "))

    elif selection == 3:

        while x == True:
            Ask_Exit = input("Would you like to continue? Y or N: ")
            if Ask_Exit == "N":
                print("You have exit the menu")
                exit()
            elif Ask_Exit == "Y":
                menu()
    
    else:
        print("Menu option not recognized, please input a number from 1 to 3")
        menu()


menu()