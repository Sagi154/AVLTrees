# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info

import math


class AVLNode(object):
	"""A class representing a node in an AVL tree"""

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

	def set_left(self, node: 'AVLNode' | None):
		"""
		sets left child.
		:param node: a node.
		"""
		self.left = node

	def set_right(self, node: 'AVLNode' | None):
		"""
		sets right child.
		:param node: a node.
		"""
		self.right = node

	def set_parent(self, node: 'AVLNode' | None):
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

	def is_node_leaf(self) -> bool:
		"""
		Checks whether node is a leaf.
		:return: True if a leaf, False otherwise.
		"""
		return not self.get_left().is_real_node() and not self.get_right().is_real_node()

	def disconnect_node_from_parent(self):
		parent = self.get_parent()
		self.set_parent(None)
		if parent.get_left() == self:
			parent.set_left(AVLNode())
		else:
			parent.set_right(AVLNode())

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

	def get_balance_factor(self) -> int:
		"""
		returns the balance factor.
		:return: the balance factor of self, 0 if the node is virtual.
		"""
		return self.bf

	def set_balance_factor(self):
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

	# TODO: move to AVLNode
	def min(self, node: AVLNode) -> AVLNode:
		while node.get_left().is_real_node():
			node = node.get_left()
		return node

	def successor(self, node: AVLNode) -> AVLNode:
		if node.get_right().is_real_node():
			return self.min(node.get_right())
		temp_parent = node.get_parent()
		while temp_parent is not None and node == temp_parent.get_right():
			node = temp_parent
			temp_parent = node.get_parent()
		return temp_parent

	def set_top_parent_post_rotation(self, post_rotate_new_top: AVLNode):
		"""
		Figures out whether the post rotation new top node is left or right child of previous top parent and sets it.
		:param post_rotate_new_top: the node at the top of the subtree post rotation.
		"""
		prev_top_parent = post_rotate_new_top.get_parent()
		if prev_top_parent is not None:
			if prev_top_parent.get_value() < post_rotate_new_top.get_value():
				prev_top_parent.set_right(post_rotate_new_top)
			else:
				prev_top_parent.set_left(post_rotate_new_top)

	def right_rotate_2(self, prev_top: AVLNode, new_top: AVLNode):
		"""
		Performs a right rotation.
		:param prev_top: The Parent of new_top, rotated to become right child of new_top.
		:param new_top: The left child of prev_top, rotated to become parent of prev_top.
		"""
		prev_top_parent = prev_top.get_parent()
		switched_sub_tree = new_top.get_right()
		new_top.set_right(prev_top)
		new_top.set_parent(prev_top_parent)
		prev_top.set_parent(new_top)
		prev_top.set_left(switched_sub_tree)
		switched_sub_tree.set_parent(prev_top)
		self.set_top_parent_post_rotation(new_top)
		self.maintain_attributes(new_top)
		self.maintain_attributes(prev_top)

	def left_rotate_2(self, prev_top: AVLNode, new_top: AVLNode):
		"""
		Performs a left rotation.
		:param prev_top: The Parent of new_top, rotated to become left child of new_top.
		:param new_top: The right child of prev_top, rotated to become parent of prev_top.
		"""
		prev_top_parent = prev_top.get_parent()
		switched_sub_tree = new_top.get_left()
		new_top.set_left(prev_top)
		new_top.set_parent(prev_top_parent)
		prev_top.set_parent(new_top)
		prev_top.set_right(switched_sub_tree)
		switched_sub_tree.set_parent(prev_top)
		self.set_top_parent_post_rotation(new_top)
		self.maintain_attributes(new_top)
		self.maintain_attributes(prev_top)

	def rotate_right(self, parent, node):
		"""
		rotate the subtree of parent to the right
		@param parent:
		@param node:
		"""

		parent.set_left(node.get_right)
		node.get_right().set_parent(parent)
		node.set_parent(parent.get_parent())
		parent.set_parent(node)
		node.set_right(parent)
		self.maintain_attributes(parent)
		self.maintain_attributes(node)
		self.set_node_parent(node)

	def rotate_left(self, parent, node):
		"""
		rotate the subtree of parent to the left
		@param parent:
		@param node:
		"""

		parent.set_right(node.get_left)
		node.get_left().set_parent(parent)
		node.set_parent(parent.get_parent())
		parent.set_parent(node)
		node.set_left(parent)
		self.maintain_attributes(parent)
		self.maintain_attributes(node)
		self.set_node_parent(node)

	def set_node_parent(self, node):
		"""
		set the node as a son of the parent after a rotation
		@param node:
		"""
		if node.parent is not None:
			if node.parent.get_value() > node.get_value():
				node.parent.set_left(node)
			node.parent.set_right(node)

	def maintain_attributes(self, node):
		"""
		Calculate and update the height, size and the balance factor of node.
		@param node: a node.
		"""
		node.set_height(1 + max(node.get_left.get_height(), node.get_right.get_height()))
		node.set_size(node.get_left.get_size() + node.get_right.get_size() + 1)
		node.set_balance_factor()

	def balance(self, node):
		"""
		check if the subtree is balanced and if not rotate him
		@param node:
		@return: the number of rotations needed to balance the tree
		"""
		node.set_balance_factor()
		num_of_rotates = 0
		if node.get_balance_factor() == -2:
			num_of_rotates += 1
			if node.get_right().get_balance_factor() > 0:
				num_of_rotates += 1
				node.get_right().rotate_right(node.get_right(), node.get_right().get_left())
			node.rotate_left(node, node.get_right())
		elif node.get_balance_factor() == 2:
			num_of_rotates += 1
			if node.left().get_balance_factor() < 0:
				num_of_rotates += 1
				node.get_left().rotate_left(node.get_left(), node.get_left().get_right())
			node.rotate_right(node, node.get_left())
		else:
			self.maintain_attributes(node)
		return num_of_rotates

	def check_balance_and_maintain_upwards(self, pointer):
		"""
		Going upwards from the parent of the inserted/ deleted node to the root and checking if each node's subtree in
		the route is balanced. If not it balance it and update the balance factory, height and size. If the subtree is
		balanced it only update the balance factory, height and size.
		The method also calculate the number of rotations needed to balance all the subtrees in the route and return
		and return it.
		@param pointer: The parent of the inserted/ deleted node
		@return: the number of rotations needed to balance all the subtrees in the route from the inserted/ deleted node
		to the root
		"""
		not_balanced = True
		num_of_rotates = 0

		while pointer is not None:
			pointer_height = pointer.get_height()
			self.maintain_attributes(pointer)
			if not_balanced:
				if abs(pointer.get_balance_factor()) < 2:
					if pointer_height == pointer.get_height():
						not_balanced = False
					else:
						pass
				else:
					num_of_rotates += self.balance(pointer)

			pointer = pointer.get_parent()
		return num_of_rotates

	def node_parent_position(self, new_node_val):
		"""
		searching for the node who will be the parent of the node that will be inserted
		@param new_node_val: the value of the node that will be inserted
		@return: the position of the node who will be the parent of the node that will be inserted
		"""
		pointer = self.root

		while pointer.is_real_node():
			tmp = pointer
			if pointer.get_value() > new_node_val:
				pointer = pointer.get_right()
			else:
				pointer = pointer.get_left()

		pointer = tmp
		return pointer

	def search(self, key: int) -> AVLNode | None:
		"""
		searches for a AVLNode in the dictionary corresponding to the key.
		:Complexity: O(log(n)) as seen in class.
		:param key: a key to be searched.
		:return: the AVLNode corresponding to key or None if key is not found.
		"""
		temp_root = self.root
		while temp_root is not None:
			if key == temp_root.key:
				return temp_root
			elif key < temp_root.key:
				temp_root = temp_root.left
			else:
				temp_root = temp_root.right
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
		node = AVLNode(key, val)

		if self.get_root() is None:
			self.root = node
			self.maintain_attributes(node)
			return 0

		node_parent = self.node_parent_position(val)

		if node_parent.get_value() > val:
			node_parent.set_right(node)
		else:
			node_parent.set_left(node)
		node.set_parent(node_parent)

		return self.check_balance_and_maintain_upwards(node_parent)

	def delete(self, node: AVLNode) -> int:
		"""
		deletes node from the dictionary.
		:param node: A real pointer to a node in self.
		:return: the number of rebalancing operation due to AVL rebalancing
		"""
		# First we perform a delete operation as in a BST.
		node_parent = self.bst_delete(node)
		return self.check_balance_and_maintain_upwards(node_parent)

	@staticmethod
	def bst_delete_has_one_child(node: AVLNode):
		"""
		? Maybe move to AVLNode ?
		Performs a delete operation on a node that has a single child.
		:param node: The node we want to delete.
		"""
		parent = node.get_parent()
		if node.get_left().is_real_node():
			child = node.get_left()
			child.set_parent(parent)
			if parent.get_left() == node:
				parent.set_left(child)
			else:
				parent.set_right(child)
		elif node.get_right().is_real_node():
			child = node.get_right()
			child.set_parent(parent)
			if parent.get_left() == node:
				parent.set_left(child)
			else:
				parent.set_right(child)
		node.set_parent(None)
		node.set_left(None)
		node.set_right(None)

	def bst_delete(self, node: AVLNode) -> AVLNode:
		"""
		Performs a delete operation on a node in a Binary Search tree and returns the parent of the physically deleted node.
		:param node: The node we want to delete.
		:return: Parent of the physically deleted node.
		"""
		parent = node.get_parent()
		# First we handle node is leaf.
		if node.is_node_leaf():
			node.disconnect_node_from_parent()
		# Second we handle node has only one real child.
		elif node.get_left().is_real_node() ^ node.get_right().is_real_node():
			self.bst_delete_has_one_child(node)
		# Last we handle node has 2 real children
		else:
			node_rep = self.successor(node)
			parent = node_rep.get_parent()
			self.bst_delete_has_one_child(node_rep)
			node.key = node_rep.key
			node.value = node_rep.value
		return parent

	def avl_to_array(self):
		return None

	def size(self) -> int:
		"""
		returns the number of items in dictionary
		:return: the number of items in dictionary
		"""
		return self.root.size

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

	def get_root(self) -> AVLNode:
		"""
		returns the root of the tree representing the dictionary.
		:return: the root, None if the dictionary is empty.
		"""
		return self.root
