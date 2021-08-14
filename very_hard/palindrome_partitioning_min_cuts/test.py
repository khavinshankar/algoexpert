'''
Given a non-empty string, write a function that returns the minimum number of cuts needed to perform 
on the string such that each remaining substring is a palindrome. A palindrome is defined as a string 
that is written the same forward as backward. Note that single-character strings are palindromes.
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.palindromePartitioningMinCuts("a"), 0)

    def test_case_2(self):
        self.assertEqual(program.palindromePartitioningMinCuts("abba"), 0)

    def test_case_3(self):
        self.assertEqual(program.palindromePartitioningMinCuts("abbba"), 0)

    def test_case_4(self):
        self.assertEqual(program.palindromePartitioningMinCuts("abb"), 1)

    def test_case_5(self):
        self.assertEqual(program.palindromePartitioningMinCuts("abbb"), 1)

    def test_case_6(self):
        self.assertEqual(program.palindromePartitioningMinCuts("noonabbad"), 2)

    def test_case_7(self):
        self.assertEqual(program.palindromePartitioningMinCuts("abcbm"), 2)

    def test_case_8(self):
        self.assertEqual(program.palindromePartitioningMinCuts("ababbbabbababa"), 3)

    def test_case_9(self):
        self.assertEqual(program.palindromePartitioningMinCuts("abbbacecffgbgffab"), 4)

    def test_case_10(self):
        self.assertEqual(
            program.palindromePartitioningMinCuts("abcdefghijklmonpqrstuvwxyz"), 25
        )

    def test_case_11(self):
        self.assertEqual(
            program.palindromePartitioningMinCuts("abcdefghijklmracecaronpqrstuvwxyz"),
            26,
        )


if __name__ == "__main__":
    unittest.main()
