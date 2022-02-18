#!/usr/bin/env python3

import unittest
from validations import validate_user

class TestValidateUser(unittest.TestCase):
	def test_valid(self):
		self.assertEqual(validate_user("validuser", 3), True)

	def test_too_short(self):
		self.assertEqual(validate_user("inv", 5), False)

	def test_invalid_characters(self):
		self.assertEqual(validate_user("invalid_user", 1), False)

	def test_negative_minlen(self):
		self.assertRaises(ValueError, validate_user, "user", -3)

#this runs the test
unittest.main()