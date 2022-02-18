#!/usr/bin/env python3

from rearrange import rearrange_name

import unittest #python library

class TestRearrange(unittest.TestCase):
	def test_basic(self):
		testcase = "Lovelace, Ada"
		expected = "Ada Lovelace"
		self.assertEqual(rearrange_name(testcase), expected)

	def test_empty(self):
		testcase = ""
		expected = ""
		self.assertEqual(rearrange_name(testcase), expected)

	def test_double_name(self):
		testcase = "Hopper, Grace M."
		expected = "Grace M. Hopper"
		self.assertEqual(rearrange_name(testcase), expected)

	def test_single_name(self):
		testcase = "Caleb"
		expected = "Caleb"
		self.assertEqual(rearrange_name(testcase), expected)



unittest.main()

'''
If the program were to fail, you would see the following:
F
======================================================================
FAIL: test_baseic (__main__.TestRearrange)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/afk/Documents/coursera/python_and_the_os/./rearrange_test.py", line 11, in test_baseic
    self.assertEqual(rearrange_name(testcase), expected)
AssertionError: 'Anda Lovelace' != 'Ada Lovelace'
- Anda Lovelace
?  -
+ Ada Lovelace


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)

'''