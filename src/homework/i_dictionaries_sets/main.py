#homework 6 main file with menu

import dictionary

def menu():

    print("Homework 6 menu, please choose an option below")
    print("1-Get p distance matrix")
    print("2-Exit")

    selection = int(input("Please choose a menu item above: "))
    x = True
    Ask_Exit = "N"

    if selection == 1:

        row_count = int(input("You have chosen get p distance matrix, enter how many rows list will have: "))
        q_count = 0
        list1 = []

        while q_count < row_count:
            sub_list = input("Enter items to be added to the list without a space or commas: ")
            int_list =[]
            for g in range(0,len(sub_list)):
                int_list.append(sub_list[g])
            list1.append(int_list)
            q_count += 1
                         
        while x == True:
            if len(list1) > 0:
                print("p distance matrix of", list1 , " is: ", dictionary.get_p_distance_matrix(list1))
                Ask_Exit = input("Would you like to exit? Y or N: ").upper()
                if Ask_Exit == "Y":
                    print("You have exit the menu")
                    exit()
                elif Ask_Exit == "N":
                    print("Staying in p distance matrix menu option")
                    row_count = int(input("You have chosen to stay in p distance matrix, enter how many rows list will have: "))
                    q_count = 0
                    list1 = []
                    while q_count < row_count:
                        sub_list = input("Enter items to be added to the list without a space or commas: ")
                        int_list =[]
                        for g in range(0,len(sub_list)):
                            int_list.append(sub_list[g])
                        list1.append(int_list)
                        q_count += 1

            elif len(list1) < 1:
                list1 = input("List is empty, enter a list: ")
    

    elif selection == 2:

        while x == True:
            Ask_Exit = input("Would you like to continue? Y or N: ").upper()
            if Ask_Exit == "N":
                print("You have exit the menu")
                exit()
            elif Ask_Exit == "Y":
                menu()
    
    else:
        print("Menu option not recognized, please input a number from 1 to 2")
        menu()


menu()