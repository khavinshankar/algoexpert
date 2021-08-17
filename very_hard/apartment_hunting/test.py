'''
You're looking to move into a new apartment, and you're given a list of blocks where each block 
contains an apartment that you could move into. In order to pick your apartment, you want to optimize 
its location. You also have a list of requirements: a list of buildings that are important to you. 
For instance, you might value having a school and a gym near your apartment. The list of blocks that 
you have contains information at every block about all of the buildings that are present and absent 
at the block in question. For instance, for every block, you might know whether a school, a pool, an 
office, and a gym are present or not. In order to optimize your life, you want to minimize the 
farthest distance you'd have to walk from your apartment to reach all of your required buildings. 
Write a function that takes in a list of blocks and a list of your required buildings and that returns 
the location (the index) of the block that is most optimal for you.
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        blocks = [
            {"gym": False, "school": True, "store": False},
            {"gym": True, "school": False, "store": False},
            {"gym": True, "school": True, "store": False},
            {"gym": False, "school": True, "store": False},
            {"gym": False, "school": True, "store": True},
        ]
        reqs = ["gym", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs), 3)

    def test_case_2(self):
        blocks = [
            {"gym": False, "office": True, "school": True, "store": False},
            {"gym": True, "office": False, "school": False, "store": False},
            {"gym": True, "office": False, "school": True, "store": False},
            {"gym": False, "office": False, "school": True, "store": False},
            {"gym": False, "office": False, "school": True, "store": True},
        ]
        reqs = ["gym", "office", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs), 2)

    def test_case_3(self):
        blocks = [
            {"gym": False, "office": True, "school": True, "store": False},
            {"gym": True, "office": False, "school": False, "store": False},
            {"gym": True, "office": False, "school": True, "store": False},
            {"gym": False, "office": False, "school": True, "store": False},
            {"gym": False, "office": False, "school": True, "store": False},
            {"gym": False, "office": False, "school": True, "store": True},
        ]
        reqs = ["gym", "office", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs) in [2, 3], True)

    def test_case_4(self):
        blocks = [
            {
                "foo": True,
                "gym": False,
                "kappa": False,
                "office": True,
                "school": True,
                "store": False,
            },
            {
                "foo": True,
                "gym": True,
                "kappa": False,
                "office": False,
                "school": False,
                "store": False,
            },
            {
                "foo": True,
                "gym": True,
                "kappa": False,
                "office": False,
                "school": True,
                "store": False,
            },
            {
                "foo": True,
                "gym": False,
                "kappa": False,
                "office": False,
                "school": True,
                "store": False,
            },
            {
                "foo": True,
                "gym": True,
                "kappa": False,
                "office": False,
                "school": True,
                "store": False,
            },
            {
                "foo": True,
                "gym": False,
                "kappa": False,
                "office": False,
                "school": True,
                "store": True,
            },
        ]
        reqs = ["gym", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs) in [4, 5], True)

    def test_case_5(self):
        blocks = [
            {"gym": True, "school": True, "store": False},
            {"gym": False, "school": False, "store": False},
            {"gym": False, "school": True, "store": False},
            {"gym": False, "school": False, "store": False},
            {"gym": False, "school": False, "store": True},
            {"gym": True, "school": False, "store": False},
            {"gym": False, "school": False, "store": False},
            {"gym": False, "school": False, "store": False},
            {"gym": False, "school": False, "store": False},
            {"gym": False, "school": True, "store": False},
        ]
        reqs = ["gym", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs), 2)

    def test_case_6(self):
        blocks = [
            {"gym": True, "pool": False, "school": True, "store": False},
            {"gym": False, "pool": False, "school": False, "store": False},
            {"gym": False, "pool": False, "school": True, "store": False},
            {"gym": False, "pool": False, "school": False, "store": False},
            {"gym": False, "pool": False, "school": False, "store": True},
            {"gym": True, "pool": False, "school": False, "store": False},
            {"gym": False, "pool": False, "school": False, "store": False},
            {"gym": False, "pool": False, "school": False, "store": False},
            {"gym": False, "pool": False, "school": False, "store": False},
            {"gym": False, "pool": False, "school": True, "store": False},
            {"gym": False, "pool": True, "school": False, "store": False},
        ]
        reqs = ["gym", "pool", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs), 7)

    def test_case_7(self):
        blocks = [
            {
                "gym": True,
                "office": False,
                "pool": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "office": True,
                "pool": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "office": True,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "pool": False,
                "school": False,
                "store": True,
            },
            {
                "gym": True,
                "office": True,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "pool": True,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "pool": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "pool": True,
                "school": False,
                "store": False,
            },
        ]
        reqs = ["gym", "pool", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs), 4)


if __name__ == "__main__":
    unittest.main()
