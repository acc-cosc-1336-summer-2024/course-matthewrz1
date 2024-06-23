#Homework 4 function creation file

def get_factorial(num):
    y = 1
    for i in range(1, num+1):
        y *= i
    return y

def sum_odd_numbers(num):
    y = 0
    i = 1
    while i <= num:
        if i % 2 == 1:
            y = y + i
            i = i + 1
        elif i % 2 == 0:
            i = i + 1
    return y
            