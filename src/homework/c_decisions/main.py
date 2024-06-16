#Main Homework 3 py file

import decisions

option = float(input("Enter an option: "))

total = int(input("Enter a total: "))

ratio = decisions.get_options_ratio(option,total)

print(decisions.get_faculty_rating(ratio))


