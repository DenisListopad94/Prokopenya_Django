from django.test import TestCase
import unittest
from .queue import UniqQueue
from django.test import TestCase


# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)


# class TestQueue(unittest.TestCase):
#
#     def test_queue_exist(self):
#         q = Queue(strategy="FIFO")
#
#     def test_exist_strategy_fifo_and_lifo(self):
#         q = Queue(strategy="FIFO")
#         with self.assertRaises(TypeError):
#             q = Queue(strategy="ABC")
#
#     def test_add_some_value_to_queue(self):
#         q = Queue(strategy="FIFO")
#         test_first_value = 4
#         q.add(test_first_value)
#         get_value = q.pop()
#         self.assertEqual(get_value, test_first_value)
# storage = [1, 2, 3, 4]


class TestUniqQueue(TestCase):

    def test_queue_exist(self):
        q = UniqQueue(strategy="LIFO")

    def test_add_some_value_to_queue(self):
        q = UniqQueue(strategy="LIFO")
        test_first_value = 4
        q.add(test_first_value)
        self.assertIn(test_first_value, q.get_queue())

    def test_add_duplicate_value_to_queue(self):
        q = UniqQueue(strategy="LIFO")
        test_value = 10
        q.add(test_value)
        result = q.add(test_value)
        self.assertEqual(result, f'Элемент {test_value} уже в очереди')
        self.assertEqual(len(q.get_queue()), 1)

    def test_exist_strategy_fifo_and_lifo(self):
        q = UniqQueue(strategy="LIFO")
        # with self.assertRaises(TypeError):
        #     q = UniqQueue(strategy="LIFO")

    def test_pop_method(self):
        q = UniqQueue(strategy="LIFO")
        test_value = 4
        q.add(test_value)
        get_value = q.pop()
        self.assertEqual(get_value, test_value)




if __name__ == '__main__':
    unittest.main()


