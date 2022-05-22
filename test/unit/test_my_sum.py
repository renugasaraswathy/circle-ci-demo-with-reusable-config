
import unittest

from src.my_sum import my_sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = my_sum(data)
        self.assertEqual(result, 6)

