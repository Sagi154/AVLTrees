#username - complete info
#id1      - complete info
#name1    - complete info
#id2      - complete info
#name2    - complete info

import math


class AVLNode(object):
	"""A class represnting a node in an AVL tree"""
	def __init__(self):
		"""
		A constructor used to create virtual nodes.
		"""
		self.key = None
		self.value = None
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0
		self.bf = 0

	def __init__(self, key: int | None, value):
		"""
		Constructor, you are allowed to add more fields.
		:param key: key or your node.
		:param value: data of your node.
		"""
		self.key = key
		self.value = value
		self.left = AVLNode()
		self.right = AVLNode()
		self.parent = None
		# TODO : figure out how height attribute maintenance should work
		self.height = 0
		self.size = 1
		"""
		The size of the sub tree this node is the root of.
		"""
		self.bf = None
		"""
		The balance factor of this node.
		"""

	def get_left(self) -> 'AVLNode' | None:
		"""
		returns the left child.
		:return: the left child of self, None if there is no left child (if self is virtual)
		"""
		return self.left

	def get_right(self) -> 'AVLNode' | None:
		"""
		returns the right child.
		:return: the right child of self, None if there is no right child (if self is virtual)
		"""
		return self.right

	def get_parent(self) -> 'AVLNode' | None:
		"""
		returns the parent.
		:return: the parent of self, None if there is no parent.
		"""
		return self.parent

	def get_key(self) -> int | None:
		"""
		returns the key.
		:return: the key of self, None if the node is virtual.
		"""
		return self.key

	def get_value(self):
		"""
		returns the value.
		:return: the value of self, None if the node is virtual.
		"""
		return self.value

	def get_height(self) -> int:
		"""
		returns the height.
		:return: the height of self, -1 if the node is virtual.
		"""
		return self.height

	def set_left(self, node: 'AVLNode'):
		"""
		sets left child.
		:param node: a node.
		"""
		self.left = node

	def set_right(self, node: 'AVLNode'):
		"""
		sets right child.
		:param node: a node.
		"""
		self.right = node

	def set_parent(self, node: 'AVLNode'):
		"""
		sets parent.
		:param node: a node.
		"""
		self.parent = node

	def set_key(self, key: int | None):
		"""
		Sets key.
		:param key: key
		"""
		self.key = key

	def set_value(self, value):
		"""
		Sets value.
		:param value: data
		"""
		self.value = value

	def set_height(self, h: int):
		"""
		sets the height of the node.
		:param h: the height of the node.
		"""
		self.height = h

	def is_real_node(self) -> bool:
		"""
		returns whether self is not a virtual node
		:return: False if self is a virtual node, True otherwise.
		"""
		return self.key is not None

	"""
			returns the height.
		:return: the height of self, -1 if the node is virtual.
	"""
	def get_size(self) -> int:
		"""
		returns the size of the node's subtree.
		:return: the size of self's subtree, 0 if the node is virtual.
		"""
		return self.size

	def set_size(self, size: int):
		"""
		Sets the size of the node.
		:param size: the size of this node.
		"""
		self.size = size

	def get_bf(self) -> int:
		"""
		returns the balance factor.
		:return: the balance factor of self, 0 if the node is virtual.
		"""
		return self.bf

	def set_bf(self):
		"""
		sets the balance factor of the node.
		"""
		self.bf = self.left.get_height() - self.right.get_height()


class AVLTree(object):
	"""
	A class implementing the ADT Dictionary, using an AVL tree.
	"""

	def __init__(self, root: AVLNode):
		"""
		Constructor, you are allowed to add more fields.

		"""
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
