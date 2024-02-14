# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info

from __future__ import annotations

import logging
import math
from printree import *


class AVLNode(object):
	"""A class representing a node in an AVL tree"""

	def __init__(self, key: int | None, value):
		"""
		Constructor, you are allowed to add more fields.
		:param key: key or your node.
		:param value: data of your node.
		"""
		if key is None:
			# Creates a virtual node
			self.key = None
			self.value = None
			self.left = None
			self.right = None
			self.parent = None
			self.height = -1
			self.size = 0
			self.bf = 0
		else:
			self.key = key
			self.value = value
			self.left = AVLNode(None, None)
			self.right = AVLNode(None, None)
			self.parent = None
			self.height = 0
			self.size = 1
			""" The size of the sub tree this node is the root of. """
			self.bf = 0
			"""
			The balance factor of this node.
			"""

	def get_left(self) -> AVLNode | None:
		"""
		returns the left child.
		:return: the left child of self, None if there is no left child (if self is virtual)
		"""
		return self.left

	def get_right(self) -> AVLNode | None:
		"""
		returns the right child.
		:return: the right child of self, None if there is no right child (if self is virtual)
		"""
		return self.right

	def get_parent(self) -> AVLNode | None:
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

	def set_left(self, node: AVLNode | None):
		"""
		sets left child.
		:param node: a node.
		"""
		self.left = node

	def set_right(self, node: AVLNode | None):
		"""
		sets right child.
		:param node: a node.
		"""
		self.right = node

	def set_parent(self, node: AVLNode | None):
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
			parent.set_left(AVLNode(None, None))
		else:
			parent.set_right(AVLNode(None, None))

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

	def maintain_attributes(self):
		"""
		Calculate and update the height, size and the balance factor of node.
		"""
		self.set_height(1 + max(self.get_left().get_height(), self.get_right().get_height()))
		self.set_size(1 + self.get_left().get_size() + self.get_right().get_size())
		self.set_balance_factor()

	def __repr__(self):
		return f"({str(self.key)} : {str(self.value)} : bf - {self.bf} : height - {self.height} : size - {self.size})"


class AVLTree(object):
	"""
	A class implementing the ADT Dictionary, using an AVL tree.
	"""

	def __init__(self, root: AVLNode):
		"""
		Constructor, you are allowed to add more fields.

		"""
		self.root = root
		self.tree_array = []

	def __repr__(self):  # no need to understand the implementation of this one
		out = ""
		for row in printree(self.root):  # need printree.py file
			out = out + row + "\n"
		return out

	# add your fields here

	@staticmethod
	def min(node: AVLNode) -> AVLNode:
		"""

		:param node:
		:return:
		"""
		while node.get_left().is_real_node():
			node = node.get_left()
		return node

	@staticmethod
	def successor(node: AVLNode) -> AVLNode:
		"""

		:param node:
		:return:
		"""
		if node.get_right().is_real_node():
			return AVLTree.min(node.get_right())
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
			if prev_top_parent.get_key() < post_rotate_new_top.get_key():
				prev_top_parent.set_right(post_rotate_new_top)
			else:
				prev_top_parent.set_left(post_rotate_new_top)

	# TODO: Figure out how to maintain attributes (in rotate or outside).
	def rotate_right(self, prev_top: AVLNode, new_top: AVLNode):
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
		prev_top.maintain_attributes()
		new_top.maintain_attributes()
		logging.debug(f"tree post left rotation with prev_top = {prev_top} and new_top = {new_top}")

	def rotate_left(self, prev_top: AVLNode, new_top: AVLNode):
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
		prev_top.maintain_attributes()
		new_top.maintain_attributes()
		logging.debug(f"tree post left rotation with prev_top = {prev_top} and new_top = {new_top}")

	def maintain_attributes(self, node):
		"""
		Calculate and update the height, size and the balance factor of node.
		@param node: a node.
		"""
		node.set_height(1 + max(node.get_left.get_height(), node.get_right.get_height()))
		node.set_size(1 + node.get_left.get_size() + node.get_right.get_size())
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
			node.maintain_attributes()
		return num_of_rotates

	def perform_balance_rotations(self, pointer: AVLNode) -> int:
		"""
		Performs the rotations needed to balance the tree.
		:param pointer: The root of the current subtree we want to balance.
		:return: Number of rotations needed to balance the tree.
		"""
		rotations = 1
		node_bf = pointer.get_balance_factor()
		if node_bf == -2:
			right_child = pointer.get_right()
			if right_child.get_balance_factor() == 1:
				self.rotate_right(prev_top=right_child, new_top=right_child.get_left())
				rotations = 2
				# right_child = right_child.get_left()
				right_child = pointer.get_right()
			self.rotate_left(prev_top=pointer, new_top=right_child)
			if self.root == pointer:
				self.root = right_child
		elif node_bf == 2:
			left_child = pointer.get_left()
			if left_child.get_balance_factor() == -1:
				self.rotate_left(prev_top=left_child, new_top=left_child.get_right())
				rotations = 2
				# left_child = left_child.get_right()
				left_child = pointer.get_left()
			self.rotate_right(prev_top=pointer, new_top=left_child)
			if self.root == pointer:
				self.root = left_child
		return rotations

	def maintain_tree_balance(self, pointer: AVLNode) -> int:
		"""
		This method makes sure the tree is balanced. It goes up the path from the
		deleted/inserted node's parent to the root and balances the tree.
		It makes sure each relevant node's attributes are maintained.
		It returns the number of nodes needed to balance the tree
		:param pointer: The parent of the inserted/ deleted node.
		:return: Number of balancing operations needed to balance the tree.
		"""
		balance_ops = 0
		while pointer is not None:
			prev_pointer_height = pointer.get_height()
			pointer.maintain_attributes()
			logging.debug("in maintain tree balance")
			logging.debug(f"pointer is{pointer}")
			bf = pointer.get_balance_factor()
			next_pointer = pointer.get_parent()
			if abs(bf) < 2 and prev_pointer_height == pointer.get_height():
				break
			elif abs(bf) < 2 and prev_pointer_height != pointer.get_height():
				balance_ops += 1
			elif abs(bf) == 2:
				balance_ops += self.perform_balance_rotations(pointer)
			logging.debug(f"pointer after rotations is{pointer}")
			pointer = next_pointer
		return balance_ops

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
			pointer.maintain_attributes()
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

	def tree_position(self, new_node_key):
		"""
		Finds insertion position of a node with a given key new_node_key.
		:param new_node_key: The key of the node we want to insert
		:return: Position of the future parent of the new node.
		"""
		pointer = self.root
		parent_position = pointer
		while pointer is not None and pointer.is_real_node():
			parent_position = pointer
			if new_node_key < pointer.key:
				pointer = pointer.get_left()
			else:
				pointer = pointer.get_right()
		return parent_position

	def node_parent_position(self, new_node_val):
		"""
		----- Fixed and changed to tree_position ----------
		---------------------------------------------------
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
		while temp_root.is_real_node():
			if key == temp_root.key:
				return temp_root
			elif key < temp_root.key:
				temp_root = temp_root.left
			else:
				temp_root = temp_root.right
		return None

	def insert(self, key: int, val) -> int:
		"""
		inserts val at position i in the dictionary
		:param key: key of item that is to be inserted to self, @pre currently does not appear in the dictionary.
		:param val: the value of the item
		:return: the number of rebalancing operation due to AVL rebalancing
		"""
		new_node = AVLNode(key, val)
		if self.get_root() is None:
			self.root = new_node
			new_node.maintain_attributes()
			return 0
		node_parent = self.tree_position(new_node.get_key())
		new_node.set_parent(node_parent)
		if new_node.get_key() > node_parent.get_key():
			node_parent.set_right(new_node)
		else:
			node_parent.set_left(new_node)
		new_node.maintain_attributes()
		# self.update_attributes(node_parent)
		logging.debug("Tree before balancing")
		logging.debug(f"\n{self}")
		return self.maintain_tree_balance(node_parent)
		# return self.check_balance_and_maintain_upwards(node_parent)

	def update_attributes(self, pointer):
		"""
		Used for testing
		:param pointer:
		:return:
		"""
		pointer.maintain_attributes()
		while pointer is not None:
			pointer.maintain_attributes()
			pointer = pointer.get_parent()

	def delete(self, node: AVLNode) -> int:
		"""
		deletes node from the dictionary.
		:param node: A real pointer to a node in self.
		:return: the number of rebalancing operation due to AVL rebalancing
		"""
		# First we perform a delete operation as in a BST.
		node_parent = self.bst_delete(node)
		# Then we balance the tree.
		return self.maintain_tree_balance(node_parent)

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

	@staticmethod
	def bst_delete_has_twins(node: AVLNode) -> AVLNode:
		# Find node successor
		node_succ = AVLTree.successor(node)
		# His parent is the parent of the physically deleted node.
		parent = node_succ.get_parent()
		# Remove node_succ from the tree
		AVLTree.bst_delete_has_one_child(node_succ)
		# replace node by node_succ
		node_succ.set_parent(node.get_parent())
		node_succ.set_left(node.get_left())
		node_succ.set_right(node.get_right())
		node.set_parent(None)
		node.set_left(None)
		node.set_right(None)
		return parent

	@staticmethod
	def bst_delete(node: AVLNode) -> AVLNode:
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
			AVLTree.bst_delete_has_one_child(node)
		# Last we handle node has 2 real children
		else:
			parent = AVLTree.bst_delete_has_twins(node)
		return parent

	def avl_to_array(self) -> list:
		"""
		returns an array representing dictionary
		:return: a sorted list according to key of touples (key, value) representing the data structure
		"""
		self.tree_array = []
		self.sorted_order(self.root)
		array = self.tree_array
		self.tree_array = []
		return array

	def sorted_order(self, node: AVLNode):
		"""
		Performs an in-order scan of the tree.
		:param node:
		"""
		if node.is_real_node():
			self.sorted_order(node.get_left())
			self.tree_array.append(node)
			self.sorted_order(node.get_right())

	def size(self) -> int:
		"""
		returns the number of items in dictionary
		:return: the number of items in dictionary
		"""
		return self.root.size

	def split(self, node: AVLNode) -> list:
		"""
		splits the dictionary at the i'th index
		:param node: The intended node in the dictionary according to whom we split, @pre node is in self
		:return: a list [left, right], where left is an AVLTree representing the keys in the
		dictionary smaller than node.key, right is an AVLTree representing the keys in the
		dictionary larger than node.key.
		"""
		left_tree_nodes: list[AVLNode] = []
		right_tree_nodes: list[AVLNode] = []
		prev_path_node = node
		temp_path_node = node.get_parent()
		# First we collect the nodes that will be used to build each tree
		while temp_path_node is not None:
			if temp_path_node.get_right() == prev_path_node:
				left_tree_nodes.append(temp_path_node)
			else:
				right_tree_nodes.append(temp_path_node)
			prev_path_node = temp_path_node
			temp_path_node = temp_path_node.get_parent()
		print(f"left list {left_tree_nodes}")
		print(f"right list {right_tree_nodes}")
		# Then we create the trees
		left_tree: AVLTree = AVLTree(left_tree_nodes[0])
		print("before first join")
		left_tree.join(tree2=AVLTree(node.get_left()), key=left_tree_nodes[0].get_key(),
						val=left_tree_nodes[0].get_value())
		right_tree: AVLTree = AVLTree(right_tree_nodes[0].get_right())
		right_tree.join(tree2=AVLTree(node.get_right()), key=right_tree_nodes[0].get_key(),
						val=right_tree_nodes[0].get_value())
		print(f"left_tree: {left_tree}")
		for left_node in left_tree_nodes[1:]:
			print(f"in for print {left_node}")
			temp_left = AVLTree(left_node.get_left())
			temp_left.join(tree2=AVLTree(left_node.get_left()), key=left_node.get_key(),
														   val=left_node.get_value())
			left_tree = temp_left
		for right_node in right_tree_nodes[1:]:
			right_tree = AVLTree(right_node.get_right()).join(tree2=right_tree, key=right_node.get_key(),
															  val=right_node.get_value())
		trees_list = [left_tree, right_tree]
		return trees_list

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
		print("------call for join---------")
		print(f"self tree is {self}")
		print(f"tree2 is {tree2}")
		print(f"node is {key} {val}")
		if (tree2.get_root() is None) or (not tree2.get_root().is_real_node()):
			if (self.get_root() is None) or (not self.get_root().is_real_node()):
				new_root = AVLNode(key, val)
				self.root = new_root
				return 1
			else:
				self.insert(key=key, val=val)
				return 1 + self.get_root().get_height()
		elif (self.get_root() is None) or (not self.get_root().is_real_node()):
			prev_tree2_height = tree2.get_root().get_height()
			tree2.insert(key=key, val=val)
			self.root = tree2.get_root()
			return 1 + prev_tree2_height

		else:
			current_tree_height = self.get_root().get_height()
			tree2_height = tree2.get_root().get_height()
			heights_difference = current_tree_height - tree2_height
			middle_node = AVLNode(key, val)

			if self.get_root().get_key() > middle_node.get_key():
				self.choose_order_and_connect(tree2.get_root(), middle_node, self.get_root())
			else:
				self.choose_order_and_connect(self.get_root(), middle_node, tree2.get_root())

			return 1 + abs(heights_difference)


	def choose_order_and_connect(self, smaller_tree_root, middle_node, bigger_tree_root):
		smaller_tree_height = smaller_tree_root.get_height()
		bigger_tree_height = bigger_tree_root.get_height()

		if smaller_tree_height > bigger_tree_height:
			subtree_of_taller_tree_root = self.get_pointer_to_highest_key_subtree_with_specific_height(smaller_tree_root ,bigger_tree_height)

			if not subtree_of_taller_tree_root.is_real_node():
				subtree_of_taller_tree_root = subtree_of_taller_tree_root.get_parent()
			self.connect_trees(subtree_of_taller_tree_root, middle_node, bigger_tree_root)
			self.root = smaller_tree_root

		elif smaller_tree_height < bigger_tree_height:
			subtree_of_taller_tree_root = self.get_pointer_to_lowest_key_subtree_with_specific_height(bigger_tree_root, smaller_tree_height)
			if not subtree_of_taller_tree_root.is_real_node():
				subtree_of_taller_tree_root = subtree_of_taller_tree_root.get_parent()
			self.connect_trees(subtree_of_taller_tree_root, middle_node, smaller_tree_root)
			self.root = bigger_tree_root

		else:
			self.connect_trees(smaller_tree_root, middle_node, bigger_tree_root)
			self.root = middle_node

		self.maintain_tree_balance(middle_node)

	def connect_trees(self, subtree_of_taller_tree, middle_node, shorter_tree_root):
		print(f"subtree {subtree_of_taller_tree}")
		if subtree_of_taller_tree.get_key() < middle_node.get_key():
			self.make_the_connection_between_the_trees(shorter_tree_root, middle_node, subtree_of_taller_tree)
		else:
			self.make_the_connection_between_the_trees(subtree_of_taller_tree, middle_node, shorter_tree_root)

	def get_pointer_to_lowest_key_subtree_with_specific_height(self, tree_root, requested_height):
		print("requested_height", requested_height)
		print(f"height of self {self.get_root()}")
		tmp_pointer = tree_root
		while tmp_pointer.get_height() > requested_height and tmp_pointer.get_left() is not None:
			print(f"pointer {tmp_pointer}")
			tmp_pointer = tmp_pointer.get_left()

		return tmp_pointer

	def get_pointer_to_highest_key_subtree_with_specific_height(self, tree_root, requested_height):
		print("requested_height", requested_height)
		print(f"height of self {self.get_root()}")
		tmp_pointer = tree_root
		while tmp_pointer.get_height() > requested_height and tmp_pointer.get_right() is not None:
			print(f"pointer {tmp_pointer}")
			tmp_pointer = tmp_pointer.get_right()

		return tmp_pointer

	""

	def make_the_connection_between_the_trees(self, bigger_tree_root, middle_node, smaller_tree_root):
		middle_node.set_left(smaller_tree_root)
		middle_node.set_right(bigger_tree_root)

		if smaller_tree_root.get_parent() is not None:
			middle_node_new_parent = smaller_tree_root.get_parent()
			middle_node.set_parent(middle_node_new_parent)
			middle_node.get_parent().set_right(middle_node)

		elif bigger_tree_root.get_parent() is not None:
			middle_node_new_parent = bigger_tree_root.get_parent()
			middle_node.set_parent(middle_node_new_parent)
			middle_node.get_parent().set_left(middle_node)

		smaller_tree_root.set_parent(middle_node)
		bigger_tree_root.set_parent(middle_node)

	def get_root(self) -> AVLNode:
		"""
		returns the root of the tree representing the dictionary.
		:return: the root, None if the dictionary is empty.
		"""
		return self.root
