import unittest
from unittest_proj.utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([]), [])
        self.assertEqual(arrs.my_slice([],3,4),[])
        self.assertEqual(arrs.my_slice([0,1,2,3,4], None, 2), [0,1])
        self.assertEqual(arrs.my_slice([1,2,3],1), [2,3])
        self.assertEqual(arrs.my_slice([1,2,3],1,33),[2,3])


