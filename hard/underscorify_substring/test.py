'''
Write a function that takes in two strings: a main string and a potential substring of the main 
string. The function should return a version of the main string with every instance of the substring 
in it wrapped between underscores. If two instances of the substring in the main string overlap each 
other or sit side by side, the underscores relevant to these two substrings should only appear on the 
far left of the left substring and on the far right of the right substring. If the main string does 
not contain the other string at all, return the main string intact.
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            program.underscorifySubstring("this is a test to see if it works", "test"),
            "this is a _test_ to see if it works",
        )

    def test_case_2(self):
        self.assertEqual(
            program.underscorifySubstring(
                "test this is a test to see if it works", "test"
            ),
            "_test_ this is a _test_ to see if it works",
        )

    def test_case_3(self):
        self.assertEqual(
            program.underscorifySubstring(
                "testthis is a test to see if it works", "test"
            ),
            "_test_this is a _test_ to see if it works",
        )

    def test_case_4(self):
        self.assertEqual(
            program.underscorifySubstring(
                "testthis is a testest to see if testestes it works", "test"
            ),
            "_test_this is a _testest_ to see if _testest_es it works",
        )

    def test_case_5(self):
        self.assertEqual(
            program.underscorifySubstring(
                "testthis is a testtest to see if testestest it works", "test"
            ),
            "_test_this is a _testtest_ to see if _testestest_ it works",
        )

    def test_case_6(self):
        self.assertEqual(
            program.underscorifySubstring(
                "this is a test to see if it works and test", "test"
            ),
            "this is a _test_ to see if it works and _test_",
        )

    def test_case_7(self):
        self.assertEqual(
            program.underscorifySubstring(
                "this is a test to see if it works and test", "bfjawkfja"
            ),
            "this is a test to see if it works and test",
        )

    def test_case_8(self):
        self.assertEqual(
            program.underscorifySubstring(
                "ttttttttttttttbtttttctatawtatttttastvb", "ttt"
            ),
            "_tttttttttttttt_b_ttttt_ctatawta_ttttt_astvb",
        )

    def test_case_9(self):
        self.assertEqual(
            program.underscorifySubstring("tzttztttz", "ttt"), "tzttz_ttt_z"
        )

    def test_case_10(self):
        self.assertEqual(
            program.underscorifySubstring(
                "abababababababababababababaababaaabbababaa", "a"
            ),
            "_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_aa_b_a_b_aaa_bb_a_b_a_b_aa_",
        )

    def test_case_11(self):
        self.assertEqual(
            program.underscorifySubstring(
                "abcabcabcabcabcabcabcabcabcabcabcabcabcabc", "abc"
            ),
            "_abcabcabcabcabcabcabcabcabcabcabcabcabcabc_",
        )


if __name__ == "__main__":
    unittest.main()
