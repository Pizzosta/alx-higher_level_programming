#!/bin/python3
""" Module for test Base class """
import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for Base class"""

    def test_id_with_no_arg(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_with_args(self):
        b1 = Base(2)
        b2 = Base(4)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 4)

    def test_private_instance(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_with_public_id(self):
        b1 = Base(10)
        b1.id = 12
        self.assertEqual(b1.id, 12)

    def test_with_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_with_float(self):
        b1 = Base(12.5)
        self.assertEqual(b1.id, 12.5)

    def test_with_dict(self):
        b1 = Base({'a': 1, 'b': 2})
        self.assertEqual(b1.id, {'a': 1, 'b': 2})

    def test_with_list(self):
        b1 = Base([1, 2, 3, 4, 5])
        self.assertEqual(b1.id, [1, 2, 3, 4, 5])

    def test_with_tuple(self):
        b1 = Base((1, 2))
        self.assertEqual(b1.id, (1, 2))

    def test_with_set(self):
        b1 = Base({1, 2})
        self.assertEqual(b1.id, {1, 2})

    def test_with_frozenset(self):
        b1 = Base(frozenset({1, 2, 3}))
        self.assertEqual(b1.id, frozenset({1, 2, 3}))

    def test_with_Nan(self):
        b1 = Base(float('nan'))
        self.assertNotEqual(b1.id, float('nan'))

    def test_with_inf(self):
        b1 = Base(float('inf'))
        self.assertEqual(b1.id, float('inf'))

    def test_with_str(self):
        b1 = Base("I am not a string")
        self.assertEqual(b1.id, 'I am not a string')

    def test_with_bool(self):
        b1 = Base(True)
        self.assertEqual(b1.id, True)

    def test_with_byte(self):
        b1 = Base(b'Bytemode')
        self.assertEqual(b1.id, b'Bytemode')

    def test_with_complex(self):
        b1 = Base(complex(5))
        self.assertEqual(b1.id, complex(5))

    def test_with_range(self):
        b1 = Base(range(5))
        self.assertEqual(b1.id, range(0, 5))

    def test_with_two_args(self):
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)


if __name__ == '__main__':
    unittest.main()

