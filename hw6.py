'''
FA18 HW6, due 11/13
Prepared by Emilio and Prithvi (and Andrew?)

Best Wishes!
REMINDER: cheating on this homework will result in a FAIR case!
'''

'''
find_ring_size

You are a secret agent in the CIA tasked with finding a ring of moles in the organization!
Rumor has it that moles hang out at Red Lion (the bar). There's a whole row of agents seated at the bar.
You start by talking to the agent seated on the left-most stool on the bar.
However, the agent redirects you to another agent.
To your great annoyance, that agent redirects you to yet another agent!!
And on and on it goes.

Standard regulation requires each agent to have a tattoo on the back of their neck
representing a unique integer, so you decide to ID each agent by their number
Each agent always redirects to a different agent,
so it is guaranteed that you will end up in an endless redirection loop.
The moles are trying to trick you by creating an endless chain of references!
Find the size of the ring and report back to headquarters.

Write a function findRing which returns the size of a loop,
given that you start by talking to the left-most agent, 0.
Numbers will be an array of non-negative integers such that
agents[m] is the number of the agent to whom agent m redirects.
agents[m] != m for all valid m, because of the above description.
The left-most agent is number 0, the next is number 1, and so on.
Each element in the numbers list will be in the range [0, n-1] where n is the length of the numbers list.

The number of agents will be at least 2.

To get full credit, your solution should run in O(n) time and space, and you must not use recursion.

This was (apparently) once a Google interview problem.

Example:
	Argument:
		[1, 3, 0, 1]
		Agent 0 redirects to agent 1, who redirects to agent 3, who redirects back to agent 1.
		There is a loop of two agent: 1, 3. Thus the answer would be 2.
		Note that even though you started with agent 0, he is not part of the ring.
	Return:
		2
'''
def find_ring_size(agents):
	pass


'''
matrix_binary_search

Given a square 2d list (matrix) of integers and a target integer,
return the 'coordinates' of the target integer as a tuple in the form (row, col)
if the element exists in the matrix, or (-1, -1) if the element does not exist.

The matrix is guaranteed to be sorted ascending row-wise,
and the zeroth element of each row is strictly larger than the last element of the previous row.
This means your solution should run in O(log n) time, where n is the total size of the input.

Your solution should use a constant amount of auxiliary space.
Otherwise, you might crash the autograder.

HUGE HINT: modify binary search.

Example 1:
	Arguments:
		[[1,2,3],[8,11,16],[23,24,25]], 8
	Return:
		(1, 0)

Example 2:
	Arguments:
		[[1,2,3],[8,11,16],[23,24,25]], 20
	Return:
		(-1, -1)
'''
def matrix_binary_search(matrix, target):
	pass


'''
rotate_matrix

Given an NxN matrix, rotate the matrix to the left 90 degrees.
This hould run in O(n) where n is the total size of the matrix. 

Example 1:
	Input: [[1,2],[3,4]]
	Return: [[2,4],[1,3]]

Example 2:
	Input: [[1,2,3],[4,5,6],[7,8,9]]
	Return: [[3,6,9],[2,5,8],[1,4,7]]
'''
def rotate_matrix(matrix):
	pass


'''
This class is provided for the next problem.
Modifying it might cause the autograder to break on delete_duplicate.
'''
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

'''
delete_duplicate

Given the head of a linked list,
delete duplicate nodes whose value has already been seen in the linked list.
Return the head of the new linked list.

This should run in O(n) time, where n is the total length of the linked list.

Example 1:
	Argument:
		1 -> 2 -> 4 -> 6 -> 4 -> 2
	Return:
		1 -> 2 -> 4 -> 6

Example 2:
	Argument:
		1 -> 1 -> 1 -> 1 -> 2
	Return:
		1 -> 2
'''
def delete_duplicate(head):
	pass


'''
next_greatest

Given a list of integers, return a new list composed of the next greater element in that list
for each index of the original index. 
More formally, given a list A, return a new list B where B[i] = A[j],
where j > i and A[j] is the first element greater than A[i]. 
If there is no such value, B[i] = -1.

This should run in O(n) time.

INPUT: An array of size n
OUTPUT: An array of size n

Example 1:
	Argument:
		[4, 5, 2, 25]
	Return:
		[5, 25, 25, -1]
		5 is the next greatest element after 4, 25 is the next greatest element after 5. etc
Example 2:
	Argument:
		[1,2,3,4,5]
	Return:
		[2,3,4,5,-1]
'''
def next_greatest(A):
	pass


'''
mcking

The McKing chain wants to open several restaurants along Red street in Shampoo-Banana.
The possible locations are at L[0], L[1], ... , L[n-1]
where L[i] is some distance in meters from the start of Red street.
Assume that the street is a straight line and the locations are in increasing order of distance
from the starting point (thus 0 <= L[0] < L[1] < . . . < L[n-1]). 
However, the city of Shampoo-Banana has a zoning law which requires that
any two McKing locations should be d or more meters apart.

Come up with an algorithm that McKing can use to figure out the next possible location for every store he has. 
If there is no store that fulfills the requirement, the next possible store should be -1.

Ex.  Let L = [0, 2, 3, 4], and d = 2

mcKing(L, d) would return the array [1, 3, -1, -1].
This is because: the restaurant at L[0] is at location 0. So, the next restaurant has to be at least 2 meters away. Note that the L[1] = 2, and is two meters away, so return_array[0] = 1
The restaurant at L[1] = 2. So, any future restaurant would have to be at location >= 4. L[3] = 4. So return_array[1] = 3
The restaurant at L[2] = 3. So, any future restaurant would have to be at locatin >= 5. There is no restaurant, so return_array[2] = -1.
The same applies for L[3] = 4. So, return_array[3] = -1

However, if d = 3

mcKing(L, d) would return the array [2, -1, -1, -1]

d will be positive.

Your algorithm should run in O(n) time for full credit
'''
def mcking(L, d):
	pass


'''
eval_exp

Given a string representing a mathematical expression,
evaluate it and return its output.

We will use the operations of addition (+), multiplication (*), and subtraction (-).
We will not use spaces in the input.
All input numbers will be non-negative integers.
All solutions will be integers.

Example 1:
	Argument:
		'3+4(6*(2-5))-127'
	Return:
		-196
Example 2:
	Argument:
		'1+1'
	Return:
		2
'''
def eval_exp(s):
	pass


