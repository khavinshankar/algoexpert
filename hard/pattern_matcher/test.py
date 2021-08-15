'''
You are given two non-empty strings. The first one is a pattern consisting of only "x"s and / or "y"s; 
the other one is a normal string of alphanumeric characters. Write a function that checks whether or 
not the normal string matches the pattern. A string S0 is said to match a pattern if replacing all 
"x"s in the pattern with some string S1 and replacing all "y"s in the pattern with some string S2 
yields the same string S0. If the input string does not match the input pattern, return an empty 
array; otherwise, return an array holding the representations of "x" and "y" in the normal string, 
in that order. If the pattern does not contain any "x"s or "y"s, the respective letter should be 
represented by an empty string in the final array that you return. Assume that there will never be 
more than one pair of strings S1 and S2 that appropriately represent "x" and "y" in the input string.
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.patternMatcher("xyxy", "abab"), ["a", "b"])

    def test_case_2(self):
        self.assertEqual(program.patternMatcher("yxyx", "abab"), ["b", "a"])

    def test_case_3(self):
        self.assertEqual(program.patternMatcher("yxx", "yomama"), ["ma", "yo"])

    def test_case_4(self):
        self.assertEqual(
            program.patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"),
            ["go", "powerranger"],
        )

    def test_case_5(self):
        self.assertEqual(
            program.patternMatcher("yyxyyx", "gogopowerrangergogopowerranger"),
            ["powerranger", "go"],
        )

    def test_case_6(self):
        self.assertEqual(
            program.patternMatcher(
                "xyxxxyyx",
                "baddaddoombaddaddoomibaddaddoombaddaddoombaddaddoombaddaddoomibaddaddoomibaddaddoom",
            ),
            ["baddaddoom", "baddaddoomi"],
        )

    def test_case_7(self):
        self.assertEqual(
            program.patternMatcher(
                "yxyyyxxy",
                "baddaddoombaddaddoomibaddaddoombaddaddoombaddaddoombaddaddoomibaddaddoomibaddaddoom",
            ),
            ["baddaddoomi", "baddaddoom"],
        )

    def test_case_8(self):
        self.assertEqual(
            program.patternMatcher("xxyxyy", "testtestwrongtestwrongtest"), []
        )

    def test_case_9(self):
        self.assertEqual(
            program.patternMatcher(
                "xyxxxyyx",
                "baddaddoombaddadoomibaddaddoombaddaddoombaddaddoombaddaddoomibaddaddoomibaddaddoom",
            ),
            [],
        )

    def test_case_10(self):
        self.assertEqual(
            program.patternMatcher("xyx", "thisshouldobviouslybewrong"), []
        )

    def test_case_11(self):
        self.assertEqual(
            program.patternMatcher("xxxx", "testtesttesttest"), ["test", ""]
        )

    def test_case_12(self):
        self.assertEqual(
            program.patternMatcher("yyyy", "testtesttesttest"), ["", "test"]
        )


if __name__ == "__main__":
    unittest.main()
