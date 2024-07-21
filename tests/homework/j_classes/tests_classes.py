#Homework 7 tests folder

import unittest

from src.homework.j_classes.class_a import Die
class Test_Config(unittest.TestCase):

    def test_die(self):
        die1 = Die()
        die1.roll()
        value1 = die1.get_rolled_value()

        die2 = Die()
        die2.roll()
        value2 = die2.get_rolled_value()

        die3 = Die()
        die3.roll()
        value3 = die3.get_rolled_value()

        if value1 >= 1 and value1 <= 6:
            assert_statement1 = True

        else:
            assert_statement1 = False

        if value2 >= 1 and value2 <= 6:
            assert_statement2 = True

        else:
            assert_statement2 = False

        if value3 >= 1 and value3 <= 6:
            assert_statement3 = True

        else:
            assert_statement3 = False

        
        self.assertEqual(True, assert_statement1)
        self.assertEqual(True, assert_statement2)
        self.assertEqual(True, assert_statement3)


