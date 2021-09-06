'''
Write a function that takes in a string and that returns its longest substring without duplicate 
characters. Assume that there will only be one longest substring without duplication.
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.longestSubstringWithoutDuplication("a"), "a")

    def test_case_2(self):
        self.assertEqual(program.longestSubstringWithoutDuplication("abc"), "abc")

    def test_case_3(self):
        self.assertEqual(program.longestSubstringWithoutDuplication("abcb"), "abc")

    def test_case_4(self):
        self.assertEqual(
            program.longestSubstringWithoutDuplication("abcdeabcdefc"), "abcdef"
        )

    def test_case_5(self):
        self.assertEqual(
            program.longestSubstringWithoutDuplication("abccdeaabbcddef"), "cdea"
        )

    def test_case_6(self):
        self.assertEqual(
            program.longestSubstringWithoutDuplication("abacacacaaabacaaaeaaafa"), "bac"
        )

    def test_case_7(self):
        self.assertEqual(
            program.longestSubstringWithoutDuplication("abcdabcef"), "dabcef"
        )

    def test_case_8(self):
        self.assertEqual(program.longestSubstringWithoutDuplication("abcbde"), "cbde")

    def test_case_9(self):
        self.assertEqual(
            program.longestSubstringWithoutDuplication("clementisacap"), "mentisac"
        )

    def test_case_10(self):
        self.assertEqual(
            program.longestSubstringWithoutDuplication("clementisanarm"), "mentisa"
        )


if __name__ == "__main__":
    unittest.main()
