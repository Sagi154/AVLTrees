#username - complete info
#id1      - complete info
#name1    - complete info
#id2      - complete info
#name2    - complete info

import math

"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields.

	@type key: int or None
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 1
		"""
		The size of the sub tree this node is the root of.
		"""
		self.bf = None
		"""
		The balance factor of this node.
		"""


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		if (self.left is None) or (self.left.key is None):
			return None
		return self.left



	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		if (self.right is None) or (self.right.key is None):
			return None
		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent


	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.left = node


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right = node


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key


	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.key!=None


	"""sets the size of the node

	@type s: int
	@param s: the size
	"""
	def set_size(self, s):
		self.size = s


	"""returns the size of the node's subtree

	@rtype: int 
	@returns: the size of self's subtree
	"""
	def get_size(self):
		return self.size


	"""sets the bf of the node

	@rtype: int
	*********************************@returns: the bf of the node
	"""

	def set_bf(self):
		self.bf = self.right.get_height() - self.left.get_height()

	"""returns the size of the node's bf

	@rtype: int
	@returns: the bf of the node
	"""

	def get_bf(self):
		return self.bf

"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self, root: AVLNode):
		self.root = root
		# add your fields here


	"""rotate the subtree of parent to the right"""
	def rotate_right(self, parent, node):
		parent.set_left(node.get_right)
		node.set_parent(parent.get_parent())
		parent.set_parent(node)
		node.set_right(parent)
		self.maintain(parent)
		self.maintain(node)
		self.set_node_parent(node)



	"""rotate the subtree of parent to the left"""
	def rotate_left(self, parent, node):
		parent.set_right(node.get_left)
		node.set_parent(parent.get_parent())
		parent.set_parent(node)
		node.set_left(parent)
		self.maintain(parent)
		self.maintain(node)
		self.set_node_parent(node)

	def set_node_parent(self,node):
		if node.parent is not None:
			if node.parent.get_value > node.get_value:
				node.parent.set_left(node)
			node.parent.set_right(node)

	def maintain(self,node):
		node.set_height(max(node.get_left.get_height(), node.get_right.get_height())+1)
		node.set_size(node.get_left.get_size() + node.get_right.get_size() + 1)
		node.set_bf()

	# blabla

	def balance(self, node):
		node.set_bf()
		if node.get_bf() > 1:
			node.rotate_left(node, node.get_left())
		elif node.get_bf() < -1:
			node.rotate_right(node, node.get_left())
		else:
			self.maintain(node)

	"""searches for a AVLNode in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	"""
	def search(self, key):
		return None


	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val):
		return -1


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		return -1


	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return None


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return -1


	"""splits the dictionary at the i'th index

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		return None


	"""joins self with key and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree2
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def join(self, tree2, key, val):
		return None


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root
