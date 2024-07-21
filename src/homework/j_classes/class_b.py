#Homework 7 testing 3 rolls

from class_a import Die

def main():

    die1 = Die()
    die2 = Die()
    die3 = Die()

    die1.roll()
    die2.roll()
    die3.roll()

    print(die1.get_rolled_value())
    print(die2.get_rolled_value())
    print(die3.get_rolled_value())

if __name__ == '__main__':
    main()



