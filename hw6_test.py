import unittest

from hw6 import *

class tester_find_ring(unittest.TestCase):
	def test_given(self):
		input = [1,3,0,1]
		self.assertEquals(find_ring_size(input), 2)

		input2 = [1,2,3,4,0]
		self.assertEquals(find_ring_size(input2), 5)

class tester_matrix_binary_search(unittest.TestCase):
	def test_given(self):
		input = [[1,2,3], [4,5,6], [7,8,9]]
		self.assertEquals(matrix_binary_search(input, 4), (1,0))
		self.assertEquals(matrix_binary_search(input, 14), (-1,-1))
 
class tester_rotate_matrix(unittest.TestCase):
	def test_given(self):
		arr1 = [[1,2],[3,4]]
		self.assertEquals(rotate_matrix(arr1), [[2,4],[1,3]])
		arr2 = [[1,2,3],[4,5,6],[7,8,9]]
		self.assertEquals(rotate_matrix(arr2), [[3,6,9],[2,5,8],[1,4,7]])

class tester_delete_duplicate(unittest.TestCase):
	def test_given(self):
		a = Node(1, Node(2, Node(3, Node(2))))
		b = delete_duplicate(a)
		self.assertEquals(b.data, 1)
		self.assertEquals(b.next_node.data, 2)
		self.assertEquals(b.next_node.next_node.data, 3)
		self.assertIsNone(b.next_node.next_node.next_node)

class tester_next_greatest(unittest.TestCase):
	def test_given(self):
		input = [4, 5, 2, 25]
		self.assertEquals(next_greatest(input), [5,25,25,-1])
		self.assertEquals(next_greatest([1,2,3,4,5]), [2,3,4,5,-1])

class tester_mc_king(unittest.TestCase):
	def test_given(self):
		self.assertEquals(mcking([0,2,3,4], 2), [1,3,-1,-1])
		self.assertEquals(mcking([0,2,3,4], 3), [2,-1,-1,-1])

class tester_eval_exp(unittest.TestCase):
	def test_given(self):
		self.assertEquals(eval_exp('3+4(6*(2-5)) - 127'), -129)
		self.assertEquals(eval_exp('1+1'), 2)
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
	