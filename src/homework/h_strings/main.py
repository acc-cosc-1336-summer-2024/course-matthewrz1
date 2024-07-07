#HW 5 

#Homework 5 main code with menu

import strings

def menu():

    print("Homework 5 menu, please choose an option below")
    print("1-Hamming Distance")
    print("2-DNA Complement")
    print("3-Exit")

    selection = int(input("Please choose a menu item above: "))
    #dna1 = ''
    #dna2 = ''
    x = True
    Ask_Exit = "N"

    if selection == 1:

        dna1 = str(input("You have chosen hamming distance, input a string with options 'A','T','C','G': "))
        print("Length of first string is ",len(dna1))
        dna2 = str(input("Input a string with options 'A','T','C','G' of same length: "))
                         
        while x == True:
            if len(dna1) == len(dna2):
                print("hamming distance of", dna1 , "and", dna2, "is: ", strings.get_hamming_distance(dna1,dna2))
                Ask_Exit = input("Would you like to exit? Y or N: ").upper()
                if Ask_Exit == "Y":
                    print("You have exit the menu")
                    exit()
                elif Ask_Exit == "N":
                    print("Staying in hamming distance menu option")
                    dna1 = str(input("input a string with options 'A','T','C','G': "))
                    dna2 = str(input("input another string with options 'A','T','C','G' of same length: " ))
            elif len(dna1) != len(dna2):
                dna1 = str(input("strings not equal, enter another 1st string: "))
                print("Length of first string is ", len(dna1))
                dna2 = str(input("Enter a 2nd string of same length: "))
    
    elif selection == 2:
        dna = str(input("You have chosen get dna complement, enter a string with options 'A','T','C','G': "))
        dna_list = ['A','T','G','C']

        while x == True:
            dna_check = True
            for h in range(0,len(dna)):
                if dna[h].upper() not in dna_list:
                    dna_check = False
                elif dna[h].upper() in dna_list:
                    dna_check = True
            
            if dna_check == True:
                print("DNA Complement of", dna, "is: ", strings.get_dna_complement(dna))
                Ask_Exit = input("Would you like to exit? Y or N: ").upper()
                if Ask_Exit == "Y":
                    print("You have exit the menu")
                    exit()
                elif Ask_Exit == "N":
                    print("Staying in dna complement menu option")
                    dna = str(input("Enter a string with options 'A','T','C','G': "))
            elif dna_check == False:
                dna = str(input("String contains letter other than 'A','T','G','C', please enter a string: "))

    elif selection == 3:

        while x == True:
            Ask_Exit = input("Would you like to continue? Y or N: ").upper()
            if Ask_Exit == "N":
                print("You have exit the menu")
                exit()
            elif Ask_Exit == "Y":
                menu()
    
    else:
        print("Menu option not recognized, please input a number from 1 to 3")
        menu()


menu()