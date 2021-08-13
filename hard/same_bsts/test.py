'''
An array of integers is said to represent the Binary Search Tree (BST) obtained by inserting each 
integer in the array (from left to right) into the BST. Write a function that takes in two arrays of 
integers and returns a boolean representing whether or not these arrays represent the same BST. Note 
that you are not allowed to construct any BSTs in your code. A BST is a Binary Tree that consists only 
of BST nodes. A node is said to be a BST node if and only if it satisfies the BST property: its value 
is strictly greater than the values of every node to its left; its value is less than or equal to the 
values of every node to its right; and both of its children nodes are either BST nodes themselves or 
None (null) values.
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        arrayOne = [1, 2, 3, 4, 5, 6, 7]
        arrayTwo = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(program.sameBsts(arrayOne, arrayTwo), True)

    def test_case_2(self):
        arrayOne = [7, 6, 5, 4, 3, 2, 1]
        arrayTwo = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(program.sameBsts(arrayOne, arrayTwo), True)

    def test_case_3(self):
        arrayOne = [10, 15, 8, 12, 94, 81, 5, 2]
        arrayTwo = [10, 8, 5, 15, 2, 12, 94, 81]
        self.assertEqual(program.sameBsts(arrayOne, arrayTwo), True)

    def test_case_4(self):
        arrayOne = [10, 15, 8, 12, 94, 81, 5, 2]
        arrayTwo = [11, 8, 5, 15, 2, 12, 94, 81]
        self.assertEqual(program.sameBsts(arrayOne, arrayTwo), False)

    def test_case_5(self):
        arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, -1, 100, 45, 12, 8, -1, 8, 2, -34]
        arrayTwo = [10, 8, 5, 15, 2, 12, 94, 81, -1, -1, -34, 8, 2, 8, 12, 45, 100]
        self.assertEqual(program.sameBsts(arrayOne, arrayTwo), True)

    def test_case_6(self):
        arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, -1, 101, 45, 12, 8, -1, 8, 2, -34]
        arrayTwo = [10, 8, 5, 15, 2, 12, 94, 81, -1, -1, -34, 8, 2, 8, 12, 45, 100]
        self.assertEqual(program.sameBsts(arrayOne, arrayTwo), False)

    def test_case_7(self):
        arrayOne = [5, 2, -1, 100, 45, 12, 8, -1, 8, 10, 15, 8, 12, 94, 81, 2, -34]
        arrayTwo = [5, 8, 10, 15, 2, 8, 12, 45, 100, 2, 12, 94, 81, -1, -1, -34, 8]
        self.assertEqual(program.sameBsts(arrayOne, arrayTwo), False)

    def test_case_8(self):
        arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, -1, 100, 45, 12, 9, -1, 8, 2, -34]
        arrayTwo = [10, 8, 5, 15, 2, 12, 94, 81, -1, -1, -34, 8, 2, 9, 12, 45, 100]
        self.assertEqual(program.sameBsts(arrayOne, arrayTwo), False)

    def test_case_9(self):
        arrayOne = [1, 2, 3, 4, 5, 6, 7, 8]
        arrayTwo = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(program.sameBsts(arrayOne, arrayTwo), False)

    def test_case_10(self):
        arrayOne = [7, 6, 5, 4, 3, 2, 1]
        arrayTwo = [7, 6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(program.sameBsts(arrayOne, arrayTwo), False)

    def test_case_11(self):
        arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 10]
        arrayTwo = [10, 8, 5, 15, 2, 10, 12, 94, 81]
        self.assertEqual(program.sameBsts(arrayOne, arrayTwo), False)

    def test_case_12(self):
        arrayOne = [50, 76, 81, 23, 23, 23, 657, 56, 12, -1, 3]
        arrayTwo = [50, 23, 76, 23, 23, 12, 56, 81, -1, 3, 657]
        self.assertEqual(program.sameBsts(arrayOne, arrayTwo), True)

    def test_case_13(self):
        arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
        arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
        self.assertEqual(program.sameBsts(arrayOne, arrayTwo), True)


if __name__ == "__main__":
    unittest.main()
