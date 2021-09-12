'''
You are given a two-dimensional array (matrix) of potentially unequal height and width containing 
only 0s and 1s. Each 0 represents land, and each 1 represents part of a river. A river consists of 
any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent). 
The number of adjacent 1s forming a river determine its size. Write a function that returns an array 
of the sizes of all rivers represented in the input matrix. Note that these sizes do not need to be 
in any particular order.


O(wh) time | O(wh) space - where w and h are the width and height of the input matrix
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        testInput = [[0]]
        expected = []
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)

    def test_case_2(self):
        testInput = [[1]]
        expected = [1]
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)

    def test_case_3(self):
        testInput = [[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]]
        expected = [1, 2, 3]
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)

    def test_case_4(self):
        testInput = [[1, 0, 0, 1], [1, 0, 1, 0], [0, 0, 1, 0], [1, 0, 1, 0]]
        expected = [1, 1, 2, 3]
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)

    def test_case_5(self):
        testInput = [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
        ]
        expected = [1, 2, 2, 2, 5]
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)

    def test_case_6(self):
        testInput = [
            [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
        ]
        expected = [1, 1, 2, 2, 5, 21]
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)

    def test_case_7(self):
        testInput = [
            [1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 1],
        ]
        expected = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)

    def test_case_8(self):
        testInput = [
            [1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 1],
        ]
        expected = [1, 1, 1, 1, 1, 1, 1, 1, 7]
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)

    def test_case_9(self):
        testInput = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
        expected = []
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)

    def test_case_10(self):
        testInput = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ]
        expected = [49]
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)

    def test_case_11(self):
        testInput = [
            [1, 1, 0, 0, 0, 0, 1, 1],
            [1, 0, 1, 1, 1, 1, 0, 1],
            [0, 1, 1, 0, 0, 0, 1, 1],
        ]
        expected = [3, 5, 6]
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)

    def test_case_12(self):
        testInput = [
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 0],
            [1, 0, 0],
            [0, 0, 0],
            [1, 0, 0],
            [1, 0, 1],
            [1, 1, 1],
        ]
        expected = [1, 1, 2, 6, 10]
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)


if __name__ == "__main__":
    unittest.main()
