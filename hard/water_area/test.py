'''
You are given an array of integers. Each non-zero integer represents the height of a pillar 
of width 1. Imagine water being poured over all of the pillars and return the surface area of 
the water trapped between the pillars viewed from the front. Note that spilled water should be 
ignored. Refer to the first minute of the video explanation below for a visual example.
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.waterArea([]), 0)

    def test_case_2(self):
        self.assertEqual(program.waterArea([0, 0, 0, 0, 0]), 0)

    def test_case_3(self):
        self.assertEqual(program.waterArea([0, 1, 0, 0, 0]), 0)

    def test_case_4(self):
        self.assertEqual(program.waterArea([0, 1, 1, 0, 0]), 0)

    def test_case_5(self):
        self.assertEqual(program.waterArea([0, 1, 2, 1, 1]), 0)

    def test_case_6(self):
        self.assertEqual(program.waterArea([0, 1, 0, 1, 0]), 1)

    def test_case_7(self):
        self.assertEqual(program.waterArea([0, 1, 0, 1, 0, 2, 0, 3]), 4)

    def test_case_8(self):
        self.assertEqual(
            program.waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]), 48
        )

    def test_case_9(self):
        self.assertEqual(
            program.waterArea([0, 8, 0, 0, 10, 0, 0, 10, 0, 0, 1, 1, 0, 3]), 49
        )

    def test_case_10(self):
        self.assertEqual(
            program.waterArea([0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 100]), 1075
        )

    def test_case_11(self):
        self.assertEqual(
            program.waterArea([0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 0]), 39
        )


if __name__ == "__main__":
    unittest.main()
