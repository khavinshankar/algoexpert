'''
Write a function that takes in a sorted array of integers as well as a target integer. The caveat is 
that the numbers in the array have been shifted by some amount; in other words, they have been moved 
to the left or the right by one or more positions. For example, [1, 2, 3, 4] might become [3, 4, 1, 2]. 
The function should use a variation of the Binary Search algorithm to find if the target number is 
contained in the array and should return its index if it is, otherwise -1.
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.shiftedBinarySearch([5, 23, 111, 1], 111), 2)

    def test_case_2(self):
        self.assertEqual(program.shiftedBinarySearch([111, 1, 5, 23], 5), 2)

    def test_case_3(self):
        self.assertEqual(program.shiftedBinarySearch([23, 111, 1, 5], 35), -1)

    def test_case_4(self):
        self.assertEqual(
            program.shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 33), 8
        )

    def test_case_5(self):
        self.assertEqual(
            program.shiftedBinarySearch([61, 71, 72, 73, 0, 1, 21, 33, 45, 45], 33), 7
        )

    def test_case_6(self):
        self.assertEqual(
            program.shiftedBinarySearch([72, 73, 0, 1, 21, 33, 45, 45, 61, 71], 72), 0
        )

    def test_case_7(self):
        self.assertEqual(
            program.shiftedBinarySearch([71, 72, 73, 0, 1, 21, 33, 45, 45, 61], 73), 2
        )

    def test_case_8(self):
        self.assertEqual(
            program.shiftedBinarySearch([73, 0, 1, 21, 33, 45, 45, 61, 71, 72], 70), -1
        )

    def test_case_9(self):
        self.assertEqual(
            program.shiftedBinarySearch(
                [33, 45, 45, 61, 71, 72, 73, 355, 0, 1, 21], 355
            ),
            7,
        )

    def test_case_10(self):
        self.assertEqual(
            program.shiftedBinarySearch(
                [33, 45, 45, 61, 71, 72, 73, 355, 0, 1, 21], 354
            ),
            -1,
        )


if __name__ == "__main__":
    unittest.main()
