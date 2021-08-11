'''
Write a function that takes in the head of a Singly Linked List that contains a loop 
(in other words, the list's tail node points to some node in the list instead of the None (null) value). 
The function should return the node (the actual node - not just its value) from which the loop 
originates in constant space. Note that every node in the Singly Linked List has a "value" property 
storing its value as well as a "next" property pointing to the next node in the list.
'''


import program
import unittest


class StartLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


linkedListClass = StartLinkedList
if hasattr(program, "LinkedList"):
    linkedListClass = program.LinkedList


class LinkedList(linkedListClass):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNthNode(self, n):
        counter = 1
        current = self
        while counter < n:
            current = current.next
            counter += 1
        return current


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test1 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test1.getNthNode(10).next = test1.getNthNode(1)
        self.assertEqual(program.findLoop(test1), test1.getNthNode(1))

    def test_case_2(self):
        test2 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test2.getNthNode(10).next = test2.getNthNode(2)
        self.assertEqual(program.findLoop(test2), test2.getNthNode(2))

    def test_case_3(self):
        test3 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test3.getNthNode(10).next = test3.getNthNode(3)
        self.assertEqual(program.findLoop(test3), test3.getNthNode(3))

    def test_case_4(self):
        test4 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test4.getNthNode(10).next = test4.getNthNode(4)
        self.assertEqual(program.findLoop(test4), test4.getNthNode(4))

    def test_case_5(self):
        test5 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test5.getNthNode(10).next = test5.getNthNode(5)
        self.assertEqual(program.findLoop(test5), test5.getNthNode(5))

    def test_case_6(self):
        test6 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test6.getNthNode(10).next = test6.getNthNode(6)
        self.assertEqual(program.findLoop(test6), test6.getNthNode(6))

    def test_case_7(self):
        test7 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test7.getNthNode(10).next = test7.getNthNode(7)
        self.assertEqual(program.findLoop(test7), test7.getNthNode(7))

    def test_case_8(self):
        test8 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test8.getNthNode(10).next = test8.getNthNode(8)
        self.assertEqual(program.findLoop(test8), test8.getNthNode(8))

    def test_case_9(self):
        test9 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test9.getNthNode(10).next = test9.getNthNode(9)
        self.assertEqual(program.findLoop(test9), test9.getNthNode(9))

    def test_case_10(self):
        test10 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test10.getNthNode(10).next = test10.getNthNode(10)
        self.assertEqual(program.findLoop(test10), test10.getNthNode(10))

    def test_case_11(self):
        test11 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test11.getNthNode(10).next = test11.getNthNode(0)
        self.assertEqual(program.findLoop(test11), test11.getNthNode(0))


if __name__ == "__main__":
    unittest.main()
