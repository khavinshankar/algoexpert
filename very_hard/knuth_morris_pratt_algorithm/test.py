'''
Write a function that takes in two strings and checks if the first string contains the second one 
using the Knuth—Morris—Pratt algorithm. The function should return a boolean.
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            program.knuthMorrisPrattAlgorithm(
                "testwafwafawfawfawfawfawfawfawfa", "fawfawfawfawfa"
            ),
            True,
        )

    def test_case_2(self):
        self.assertEqual(
            program.knuthMorrisPrattAlgorithm(
                "tesseatesgawatewtesaffawgfawtteafawtesftawfawfawfwfawftest", "test"
            ),
            True,
        )

    def test_case_3(self):
        self.assertEqual(
            program.knuthMorrisPrattAlgorithm("aaabaabacdedfaabaabaaa", "aabaabaaa"),
            True,
        )

    def test_case_4(self):
        self.assertEqual(
            program.knuthMorrisPrattAlgorithm("abxabcabcaby", "abcaby"), True
        )

    def test_case_5(self):
        self.assertEqual(program.knuthMorrisPrattAlgorithm("decadaafcdf", "daf"), False)

    def test_case_6(self):
        self.assertEqual(
            program.knuthMorrisPrattAlgorithm("aefoaefcdaefcdaed", "aefcdaed"), True
        )

    def test_case_7(self):
        self.assertEqual(
            program.knuthMorrisPrattAlgorithm("aefoaefcdaefcdaed", "aefcaefaeiaefcd"),
            False,
        )

    def test_case_8(self):
        self.assertEqual(
            program.knuthMorrisPrattAlgorithm(
                "aefcdfaecdaefaefcdaefeaefcdcdeae", "aefcdaefeaefcd"
            ),
            True,
        )

    def test_case_9(self):
        self.assertEqual(
            program.knuthMorrisPrattAlgorithm("bccbefbcdabbbcabfdcfe", "abc"), False
        )

    def test_case_10(self):
        self.assertEqual(
            program.knuthMorrisPrattAlgorithm("adafccfefbbbfeeccbcfd", "ecb"), False
        )

    def test_case_11(self):
        self.assertEqual(
            program.knuthMorrisPrattAlgorithm(
                "testwherethefullstringmatches", "testwherethefullstringmatches"
            ),
            True,
        )


if __name__ == "__main__":
    unittest.main()
