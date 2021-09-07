'''
Write a function that takes in a sorted array of integers as well as a target integer. The function 
should use a variation of the Binary Search algorithm to find a range of indices in between which the 
target number is contained in the array and should return this range in the form of an array. The 
first number in the output array should represent the first index at which the target number is 
located while the second number should represent the last index at which the target number is located. 
The function should return [-1, -1] if the number is not contained in the array.
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.searchForRange([5, 7, 7, 8, 8, 10], 5), [0, 0])

    def test_case_2(self):
        self.assertEqual(program.searchForRange([5, 7, 7, 8, 8, 10], 7), [1, 2])

    def test_case_3(self):
        self.assertEqual(program.searchForRange([5, 7, 7, 8, 8, 10], 8), [3, 4])

    def test_case_4(self):
        self.assertEqual(program.searchForRange([5, 7, 7, 8, 8, 10], 10), [5, 5])

    def test_case_5(self):
        self.assertEqual(program.searchForRange([5, 7, 7, 8, 8, 10], 9), [-1, -1])

    def test_case_6(self):
        self.assertEqual(
            program.searchForRange(
                [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 47
            ),
            [-1, -1],
        )

    def test_case_7(self):
        self.assertEqual(
            program.searchForRange(
                [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], -1
            ),
            [-1, -1],
        )

    def test_case_8(self):
        self.assertEqual(
            program.searchForRange(
                [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45
            ),
            [4, 9],
        )

    def test_case_9(self):
        self.assertEqual(
            program.searchForRange(
                [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 45, 45, 45], 45
            ),
            [4, 12],
        )


if __name__ == "__main__":
    unittest.main()
