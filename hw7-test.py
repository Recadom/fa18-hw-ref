#!/usr/bin/python3

# standard boilerplate

import unittest
from hw7 import *

#====================================


class tester_max_nesting(unittest.TestCase):
	
	def test__given(self):
		self.assertEqual(max_nesting([[3, 4], [2, 3]]), 2)
		self.assertEqual(max_nesting([[[3, 4], 3], 4]), 3)
		
		a = [[3], [2, 3]]
		a[0][0] = a
		self.assertEqual(max_nesting(a), -2)
		self.assertEqual(max_nesting([[a]]), -4)


class tester_almost_product(unittest.TestCase):
	
	def test__given(self):
		given = [[2,3,4,5], [3,6,9,-3,2,-2]]
		ex = [[60, 40, 30, 24], [648, 324, 216, -648, 972, -972]]
		
		for i in range(len(given)):
			self.assertEqual(almost_product(given), ex)


class tester_staircase_ways(unittest.TestCase):
	
	def test__given(self):
		g_sta = [3, 3, 5]
		g_ste = [0, 1, 2]
		ex = [1, 3, 13]
		
		for i in range(len(g_sta)):
			self.assertEqual(staircase_ways(g_sta[i], g_ste[i]), ex[i])


class tester_longest_increasing_subsequence(unittest.TestCase):
	
	def test__given(self):
		self.assertEqual(longest_increasing_subsequence([3, 2, 6, 4, 5, 8]), 4)


class tester_edit_distance(unittest.TestCase):
	
	def test__given(self):
		self.assertEqual(edit_distance('kitten', 'sitting'), 3)


class tester_maximal_sum_subarray(unittest.TestCase):
	
	def test__given(self):
		self.assertEqual(tuple(maximal_sum_subarray([-8, -6, 1, -4, 3, 4, 6])), (4, 6))
		self.assertEqual(tuple(maximal_sum_subarray([0])), (0, 1))
		self.assertEqual(tuple(maximal_sum_subarray([-1, 0])), (1, 1))


class tester_longest_palindromic_substring(unittest.TestCase):
	
	def test__given(self):
		self.assertEqual(tuple(longest_palindromic_substring('ABBAC')), (0, 4))
		self.assertEqual(tuple(longest_palindromic_substring('A')), (0, 1))
	


#===================================

# suppress stdout, but keep stderr since that's what unittest uses
# https://stackoverflow.com/questions/30715337

from io import StringIO
import sys

class ReplaceStd(object):
	""" Let's make it pythonic. """

	def __init__(self):
		self.stdout = None
		#self.stderr = None

	def __enter__(self):
		self.stdout = sys.stdout
		#self.stderr = sys.stderr

		# as it was suggested already:
		sys.stdout = StringIO()
		#sys.stderr = StringIO()

	def __exit__(self, type, value, traceback):
		sys.stdout.close()
		#sys.stderr.close()
		
		sys.stdout = self.stdout
		#sys.stderr = self.stderr

if __name__ == "__main__":
	
	with ReplaceStd():
		unittest.main(module=__name__, buffer=True, exit=False)
