import unittest
from hamcrest import *
import lab1
from sympy import sqrt

param = [['№1', 1, 2], ['№2', 2, 3], ['№3', 3, 4]]

class Lab1Test(unittest.TestCase):
    """Lab1 tests"""

    def setUp(self):  #todo @Before
        self.x_arr = [10, 4, 0, 3, 0]

    @classmethod
    def setUpClass(cls): #todo @Beforeclass
        cls.x_arr = [10, 4, 0, 3, 0]

    def test_f(self):
        self.assertEqual(lab1.f(7), sqrt(1+2*7**2-7**3))

    def test_listsum(self):
        self.assertNotEqual(lab1.listsum(self.x_arr), 16)

    def test_paired_array_f(self):
        self.assertEqual(lab1.paired_array_f(self.x_arr), [sqrt(1+2*(0**2)-0**3)])

    def test_unpaired_array_f(self):
        self.assertEqual(lab1.unpaired_array_f(self.x_arr), [sqrt(1+2*(4**2)-4**3), sqrt(1+2*(3**2)-3**3)])

    def test_h_is_formula(self):
        self.assertTrue(lab1.s, lab1.av)

    def test_x_arr_is_not_none(self):
        self.assertIsNotNone(lab1.x_array)

    def testEquals(self): #todo hamcrest
        assert_that(lab1.paired_array_f(self.x_arr), equal_to([sqrt(1+2*(0**2)-0**3)]))
    
    def test_close_to(self): #todo hamcrest
        assert_that(lab1.s, close_to(1.09, 0.01))


def test_generator(a, b):
    def test(self):
        self.assertNotEqual(a, b)

    return test

if __name__ == '__main__':
    for t in param:
        test_name = 'test_%s' % t[0]
        test = test_generator(t[1], t[2])
        setattr(Lab1Test, test_name, test)
    unittest.main()