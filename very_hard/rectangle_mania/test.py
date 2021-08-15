'''
Write a function that takes in a list of Cartesian coordinates (i.e., (x, y) coordinates) and returns 
the number of rectangles formed by these coordinates. Note that a rectangle must have four corners 
present in order to be counted, and we only care about rectangles with sides parallel to the x and y 
axes (i.e., with horizontal and vertical sides--no diagonal sides). You can also assume that no 
coordinate will be farther than 100 units from the origin.
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        coords = [[0, 0], [0, 1], [1, 1], [1, 0]]
        self.assertEqual(program.rectangleMania(coords), 1)

    def test_case_2(self):
        coords = [[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0]]
        self.assertEqual(program.rectangleMania(coords), 3)

    def test_case_3(self):
        coords = [[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0], [3, 1], [3, 0]]
        self.assertEqual(program.rectangleMania(coords), 6)

    def test_case_4(self):
        coords = [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 0],
            [2, 1],
            [2, 0],
            [3, 1],
            [3, 0],
            [1, 3],
            [3, 3],
        ]
        self.assertEqual(program.rectangleMania(coords), 8)

    def test_case_5(self):
        coords = [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 0],
            [2, 1],
            [2, 0],
            [3, 1],
            [3, 0],
            [1, 3],
            [3, 3],
            [0, -4],
            [3, -4],
        ]
        self.assertEqual(program.rectangleMania(coords), 10)

    def test_case_6(self):
        coords = [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 0],
            [2, 1],
            [2, 0],
            [3, 1],
            [3, 0],
            [1, 3],
            [3, 3],
            [0, -4],
            [3, -4],
            [1, -3],
            [3, -3],
        ]
        self.assertEqual(program.rectangleMania(coords), 13)

    def test_case_7(self):
        coords = [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 0],
            [2, 1],
            [2, 0],
            [3, 1],
            [3, 0],
            [1, 3],
            [3, 3],
            [0, -4],
            [3, -4],
            [1, -3],
            [3, -3],
            [-1, 0],
            [-10, 0],
            [-1, -1],
            [2, -2],
        ]
        self.assertEqual(program.rectangleMania(coords), 13)

    def test_case_8(self):
        coords = [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 0],
            [2, 1],
            [2, 0],
            [3, 1],
            [3, 0],
            [1, 3],
            [3, 3],
            [0, -4],
            [3, -4],
            [1, -3],
            [3, -3],
            [-1, 0],
            [-10, 0],
            [-1, -1],
            [2, -2],
            [0, -1],
            [1, -4],
            [-10, -4],
        ]
        self.assertEqual(program.rectangleMania(coords), 23)

    def test_case_9(self):
        coords = [
            [0, 0],
            [0, 1],
            [1, 0],
            [2, 1],
            [1, 3],
            [3, 3],
            [0, -4],
            [3, -5],
            [1, -3],
            [3, -2],
            [-1, 0],
            [-10, 0],
            [-1, -1],
            [2, -2],
        ]
        self.assertEqual(program.rectangleMania(coords), 0)

    def test_case_10(self):
        coords = [[0, 0], [0, 1], [1, 1]]
        self.assertEqual(program.rectangleMania(coords), 0)


if __name__ == "__main__":
    unittest.main()
