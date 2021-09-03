'''
You are given a non-empty array of arrays. Each subarray holds three integers and represents a disk. 
These integers denote each disk's width, depth, and height, respectively. Your goal is to stack up the 
disks and to maximize the total height of the stack. A disk must have a strictly smaller width, depth, 
and height than any other disk below it. Write a function that returns an array of the disks in the 
final stack, starting with the top disk and ending with the bottom disk. Note that you cannot rotate 
disks; in other words, the integers in each subarray must represent [width, depth, height] at all 
times. Assume that there will only be one stack with the greatest total height.
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.diskStacking([[2, 1, 2]]), [[2, 1, 2]])

    def test_case_2(self):
        self.assertEqual(
            program.diskStacking([[2, 1, 2], [3, 2, 3]]), [[2, 1, 2], [3, 2, 3]]
        )

    def test_case_3(self):
        self.assertEqual(
            program.diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8]]), [[2, 2, 8]]
        )

    def test_case_4(self):
        self.assertEqual(
            program.diskStacking([[2, 1, 2], [3, 2, 3], [2, 3, 4]]),
            [[2, 1, 2], [3, 2, 3]],
        )

    def test_case_5(self):
        self.assertEqual(
            program.diskStacking(
                [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]
            ),
            [[2, 1, 2], [3, 2, 3], [4, 4, 5]],
        )

    def test_case_6(self):
        self.assertEqual(
            program.diskStacking(
                [[2, 1, 2], [3, 2, 5], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]
            ),
            [[2, 3, 4], [4, 4, 5]],
        )

    def test_case_7(self):
        self.assertEqual(
            program.diskStacking(
                [
                    [2, 1, 2],
                    [3, 2, 3],
                    [2, 2, 8],
                    [2, 3, 4],
                    [1, 2, 1],
                    [4, 4, 5],
                    [1, 1, 4],
                ]
            ),
            [[1, 1, 4], [2, 2, 8]],
        )

    def test_case_8(self):
        self.assertEqual(
            program.diskStacking(
                [
                    [3, 3, 4],
                    [2, 1, 2],
                    [3, 2, 3],
                    [2, 2, 8],
                    [2, 3, 4],
                    [5, 5, 6],
                    [1, 2, 1],
                    [4, 4, 5],
                    [1, 1, 4],
                    [2, 2, 3],
                ]
            ),
            [[2, 2, 3], [3, 3, 4], [4, 4, 5], [5, 5, 6]],
        )


if __name__ == "__main__":
    unittest.main()
