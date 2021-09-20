'''
Given a non-empty array of integers, write a function that returns the longest 
strictly-increasing subsequence of the array. A subsequence is defined as a set of numbers 
that are not necessarily adjacent but that are in the same order as they appear in the array. 
Assume that there will only be one longest increasing subsequence.
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.longestIncreasingSubsequence([-1]), [-1])

    def test_case_2(self):
        self.assertEqual(program.longestIncreasingSubsequence([-1, 2]), [-1, 2])

    def test_case_3(self):
        self.assertEqual(
            program.longestIncreasingSubsequence([-1, 2, 1, 2]), [-1, 1, 2]
        )

    def test_case_4(self):
        self.assertEqual(
            program.longestIncreasingSubsequence([1, 5, -1, 10]), [1, 5, 10]
        )

    def test_case_5(self):
        self.assertEqual(
            program.longestIncreasingSubsequence([1, 5, -1, 0, 6, 2, 4]), [-1, 0, 2, 4]
        )

    def test_case_6(self):
        self.assertEqual(program.longestIncreasingSubsequence([3, 4, -1]), [3, 4])

    def test_case_7(self):
        self.assertEqual(
            program.longestIncreasingSubsequence([29, 2, 32, 12, 30, 31]),
            [2, 12, 30, 31],
        )

    def test_case_8(self):
        self.assertEqual(
            program.longestIncreasingSubsequence(
                [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
            ),
            [-24, 2, 3, 5, 6, 35],
        )

    def test_case_9(self):
        self.assertEqual(
            program.longestIncreasingSubsequence([10, 22, 9, 33, 21, 61, 41, 60, 80]),
            [10, 22, 33, 41, 60, 80],
        )

    def test_case_10(self):
        self.assertEqual(
            program.longestIncreasingSubsequence([100, 1, 2, 3, 4, 101]),
            [1, 2, 3, 4, 101],
        )


if __name__ == "__main__":
    unittest.main()
