'''
Given a list of strings, write a function that returns the longest string chain that can be built from 
those strings. A string chain is defined as follows: let string A be a string in the initial array; 
if removing any single character from string A yields a new string B that is contained in the initial 
array of strings, then strings A and B form a string chain of length 2. Similarly, if removing any 
single character from string B yields a new string C that is contained in the initial array of strings, 
then strings A, B, and C form a string chain of length 3. The function should return the string chain 
in descending order (i.e., from the longest string to the shortest one). Note that string chains of 
length 1 do not exist; if the list of strings does not contain any string chain formed by 2 or more 
strings, the function should return an empty list.
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        strings = ["abcdefg", "abcdef", "abcde", "abcd", "abc", "ab", "a"]
        expected = ["abcdefg", "abcdef", "abcde", "abcd", "abc", "ab", "a"]
        self.assertEqual(program.longestStringChain(strings), expected)

    def test_case_2(self):
        strings = ["abcdefg", "abdefg", "abdfg", "bdfg", "bfg", "bg", "g"]
        expected = ["abcdefg", "abdefg", "abdfg", "bdfg", "bfg", "bg", "g"]
        self.assertEqual(program.longestStringChain(strings), expected)

    def test_case_3(self):
        strings = [
            "abcdefg",
            "1234",
            "abdefg",
            "abdfg",
            "123",
            "12",
            "bg",
            "g",
            "12345",
            "12a345",
        ]
        expected = ["12a345", "12345", "1234", "123", "12"]
        self.assertEqual(program.longestStringChain(strings), expected)

    def test_case_4(self):
        strings = [
            "abcdefg1",
            "1234c",
            "abdefg2",
            "abdfg",
            "123",
            "122",
            "bgg",
            "g",
            "1a2345",
            "12a345",
        ]
        expected = []
        self.assertEqual(program.longestStringChain(strings), expected)

    def test_case_5(self):
        strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]
        expected = ["abcdef", "abcde", "abde", "ade", "ae"]
        self.assertEqual(program.longestStringChain(strings), expected)

    def test_case_6(self):
        strings = [
            "lgoprt",
            "12345678",
            "algoxpert",
            "abcde",
            "123468",
            "lgoxprt",
            "abde",
            "lgopt",
            "1234678",
            "ade",
            "ae",
            "algoxprt",
            "a",
            "1abde",
            "lgpt",
            "123456789",
            "234678",
            "algoexpert",
        ]
        expected = [
            "algoexpert",
            "algoxpert",
            "algoxprt",
            "lgoxprt",
            "lgoprt",
            "lgopt",
            "lgpt",
        ]
        self.assertEqual(program.longestStringChain(strings), expected)

    def test_case_7(self):
        strings = [
            "12345678",
            "algoxpert",
            "123468",
            "abde",
            "lgopt",
            "1234678",
            "ade",
            "ae",
            "a",
            "1abde",
            "lgpt",
            "123456789",
            "234678",
            "algoexpert",
        ]
        expected = ["1abde", "abde", "ade", "ae", "a"]
        self.assertEqual(program.longestStringChain(strings), expected)


if __name__ == "__main__":
    unittest.main()
