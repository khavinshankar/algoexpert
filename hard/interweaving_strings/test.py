'''
Write a function that takes in three strings and returns a boolean representing whether or not the 
third string can be formed by interweaving the first two strings. To interweave strings means to merge 
them by alternating their letters without any specific pattern. For instance, the strings "abc" and 
"123" can be interwoven as "a1b2c3", as "abc123", and as "ab1c23" (this list is nonexhaustive).
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        one = "a"
        two = "b"
        three = "ab"
        self.assertEqual(program.interweavingStrings(one, two, three), True)

    def test_case_2(self):
        one = "a"
        two = "b"
        three = "ba"
        self.assertEqual(program.interweavingStrings(one, two, three), True)

    def test_case_3(self):
        one = "a"
        two = "b"
        three = "ac"
        self.assertEqual(program.interweavingStrings(one, two, three), False)

    def test_case_4(self):
        one = "abc"
        two = "def"
        three = "abcdef"
        self.assertEqual(program.interweavingStrings(one, two, three), True)

    def test_case_5(self):
        one = "abc"
        two = "def"
        three = "abdecf"
        self.assertEqual(program.interweavingStrings(one, two, three), True)

    def test_case_6(self):
        one = "abc"
        two = "def"
        three = "deabcf"
        self.assertEqual(program.interweavingStrings(one, two, three), True)

    def test_case_7(self):
        one = "aabcc"
        two = "dbbca"
        three = "aadbbcbcac"
        self.assertEqual(program.interweavingStrings(one, two, three), True)

    def test_case_8(self):
        one = "aabcc"
        two = "dbbca"
        three = "aadbbbaccc"
        self.assertEqual(program.interweavingStrings(one, two, three), False)

    def test_case_9(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjob"
        self.assertEqual(program.interweavingStrings(one, two, three), True)

    def test_case_10(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "ayloguore-xdpreeratm-job"
        self.assertEqual(program.interweavingStrings(one, two, three), True)

    def test_case_11(self):
        one = "aaaaaaa"
        two = "aaaabaaa"
        three = "aaaaaaaaaaaaaab"
        self.assertEqual(program.interweavingStrings(one, two, three), False)

    def test_case_12(self):
        one = "aaaaaaa"
        two = "aaaaaaa"
        three = "aaaaaaaaaaaaaa"
        self.assertEqual(program.interweavingStrings(one, two, three), True)

    def test_case_13(self):
        one = "aacaaaa"
        two = "aaabaaa"
        three = "aaaabacaaaaaaa"
        self.assertEqual(program.interweavingStrings(one, two, three), True)

    def test_case_14(self):
        one = "aacaaaa"
        two = "aaabaaa"
        three = "aaaacabaaaaaaa"
        self.assertEqual(program.interweavingStrings(one, two, three), True)

    def test_case_15(self):
        one = "aacaaaa"
        two = "aaabaaa"
        three = "aaaaaacbaaaaaa"
        self.assertEqual(program.interweavingStrings(one, two, three), False)

    def test_case_16(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "1your-algodream-expertjob"
        self.assertEqual(program.interweavingStrings(one, two, three), False)

    def test_case_17(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjob1"
        self.assertEqual(program.interweavingStrings(one, two, three), False)

    def test_case_18(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjo"
        self.assertEqual(program.interweavingStrings(one, two, three), False)


if __name__ == "__main__":
    unittest.main()
