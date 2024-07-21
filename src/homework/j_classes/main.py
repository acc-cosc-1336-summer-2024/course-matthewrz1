#Homework 7 main file with menu

import class_a
from class_a import Die

def menu():

    print("Homework 7 menum, please choose an option below:")
    print("1-Roll die")
    print("2-Exit")

    selection = int(input("Please choose a menu item: "))
    x = True
    Ask_Exit = "N"

    die1 = Die()
    die1.roll()
    rolled_value = die1.get_rolled_value()

    if selection == 1:
        while x == True:
            if rolled_value > 0:
                print("Rolling die...")
                print("Value of rolled dice is: ", rolled_value)
                Ask_Exit = input("Would you like to exit? Y or N: ").upper()
                if Ask_Exit == "Y":
                    print("You have exit the menu")
                    exit()
                elif Ask_Exit == "N":
                    print("Staying in die roll menu")
                    die1.roll()
                    rolled_value = die1.get_rolled_value()
    
    elif selection == 2:

        while x == True:
            Ask_Exit = input("Would you like to continue? Y or N: ").upper()
            if Ask_Exit == "N":
                print("You have exit the menu")
                exit()
            elif Ask_Exit == "Y":
                menu()

menu()
