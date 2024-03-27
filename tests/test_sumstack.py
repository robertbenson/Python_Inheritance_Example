import unittest
from Stack import SumStack


class SumstackTestCase(unittest.TestCase):

    def test_sum_10(self):
        """ range 0,1,2,3,4 """
        adding_stack = SumStack()

        for i in range(5):
            adding_stack.push(i)
        self.assertEqual(adding_stack.get_sum(), 10)

    def test_sum_111100(self):
        """ push 4 amounts (2 int,2 float) to the stack,
        then get sum and pop each amount. Check popped amount and new sum
        each time"""
        adding_stack = SumStack()

        adding_stack.push(100.00)
        adding_stack.push(1000)
        adding_stack.push(10000.00)
        adding_stack.push(100000)
        self.assertEqual(adding_stack.get_sum(), 111100)
        self.assertEqual(adding_stack.pop(), 100000)
        self.assertEqual(adding_stack.get_sum(), 11100)
        self.assertEqual(adding_stack.pop(), 10000)
        self.assertEqual(adding_stack.get_sum(), 1100)
        self.assertEqual(adding_stack.pop(), 1000)
        self.assertEqual(adding_stack.get_sum(), 100)
        self.assertEqual(adding_stack.pop(), 100)
        self.assertEqual(adding_stack.get_sum(), 0)

    def test_sum_negative_values(self):
        """ push negative amounts to the stack,
        then get sum and pop each amount. Check popped amount and new sum
        each time"""
        adding_stack = SumStack()

        adding_stack.push(-12.34)
        self.assertEqual(adding_stack.get_sum(), -12.34)
        adding_stack.push(10.00)
        self.assertEqual(adding_stack.get_sum(), -2.34)
        self.assertEqual(adding_stack.pop(), 10)
        self.assertEqual(adding_stack.get_sum(), -12.34)
        self.assertEqual(adding_stack.pop(), -12.34)
        self.assertEqual(adding_stack.get_sum(), 0)


    def test_push_non_int(self):
        """ the stack should only accept integers"""
        adding_stack = SumStack()
        with self.assertRaises(TypeError) as context:
            adding_stack.push('A')

        with self.assertRaises(TypeError) as context:
            adding_stack.push('')


if __name__ == '__main__':
    unittest.main()
