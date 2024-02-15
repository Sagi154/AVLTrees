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
		if parent is not None:
			if parent.get_left() == self:
				parent.set_left(AVLNode(None, None))
			else:
				parent.set_right(AVLNode(None, None))

	def disconnect_node_from_children(self):
		if self.get_left().is_real_node():
			self.get_left().set_parent(None)
			self.set_left(AVLNode(None, None))
		if self.get_right().is_real_node():
			self.get_right().set_parent(None)
			self.set_right(AVLNode(None, None))

	def clear_node_from_pointers(self):
		self.disconnect_node_from_parent()
		self.disconnect_node_from_children()

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

	def rotate_right(self, prev_top: AVLNode, new_top: AVLNode):
		"""
		Performs a right rotation.
		:param prev_top: The Parent of new_top, rotated to become right child of new_top.
		:param new_top: The left child of prev_top, rotated to become parent of prev_top.
		"""
		prev_top_parent = prev_top.get_parent()
		switched_sub_tree = new_top.get_right()

		if switched_sub_tree is None:
			logging.warning(f"\n switched is None")

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

		if switched_sub_tree is None:
			logging.warning(f"\n switched is None")

		new_top.set_left(prev_top)
		new_top.set_parent(prev_top_parent)
		prev_top.set_parent(new_top)
		prev_top.set_right(switched_sub_tree)
		switched_sub_tree.set_parent(prev_top)
		self.set_top_parent_post_rotation(new_top)
		prev_top.maintain_attributes()
		new_top.maintain_attributes()
		logging.debug(f"tree post left rotation with prev_top = {prev_top} and new_top = {new_top}")

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
			# if pointer.get_left() == None or pointer.get_right() == None:
			# 	# print(f"tree is {self}")
			# 	# print(f"the pointer is {pointer}")
			# 	# print(f"parent is {pointer.get_parent()}")
			# 	# print(f"the left child is {pointer.get_left()}")
			# 	# print(f"the right child is {pointer.get_right()}")
			prev_pointer_height = pointer.get_height()
			pointer.maintain_attributes()
			bf = pointer.get_balance_factor()
			next_pointer = pointer.get_parent()
			if abs(bf) < 2 and prev_pointer_height == pointer.get_height():
				break
			elif abs(bf) < 2 and prev_pointer_height != pointer.get_height():
				balance_ops += 1
			elif abs(bf) == 2:
				balance_ops += self.perform_balance_rotations(pointer)
			pointer = next_pointer
		# If reached break, Keep going to root so size can be maintained.
		if pointer is not None and pointer.get_parent() is not None:
			pointer = pointer.get_parent()
			pointer.maintain_attributes()
		return balance_ops

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

	def search(self, key: int) -> AVLNode | None:
		"""
		searches for a AVLNode in the dictionary corresponding to the key.
		:Complexity: O(log(n)) as seen in class.
		:param key: a key to be searched.
		:return: the AVLNode corresponding to key or None if key is not found.
		"""
		temp_node = self.root
		if temp_node is None:
			return None
		while temp_node.is_real_node():
			if key == temp_node.key:
				return temp_node
			elif key < temp_node.key:
				temp_node = temp_node.left
			else:
				temp_node = temp_node.right
		return None

	def insert(self, key: int, val) -> int:
		"""
		inserts val at position i in the dictionary
		:param key: key of item that is to be inserted to self, @pre currently does not appear in the dictionary.
		:param val: the value of the item
		:return: the number of rebalancing operation due to AVL rebalancing
		"""
		new_node = AVLNode(key, val)
		if self.get_root() is None or not self.get_root().is_real_node():
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
		return self.maintain_tree_balance(node_parent)
		# return self.check_balance_and_maintain_upwards(node_parent)

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

	def bst_delete_has_one_child(self, node: AVLNode):
		"""
		? Maybe move to AVLNode ?
		Performs a delete operation on a node that has a single child.
		:param node: The node we want to delete.
		"""
		parent = node.get_parent()
		if self.root == node:
			if node.get_left().is_real_node():
				self.root = node.get_left()
				node.get_left().set_parent(None)
			else:
				node.get_right().set_parent(None)
				self.root = node.get_right()
		elif node.get_left().is_real_node():
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
		node.set_left(AVLNode(None, None))
		node.set_right(AVLNode(None, None))

	def bst_delete_has_twins(self, node: AVLNode) -> AVLNode:
		# Find node successor
		node_succ = AVLTree.successor(node)
		# His parent is the parent of the physically deleted node.
		parent = node_succ.get_parent()
		if parent == node:
			parent = node_succ
		# Remove node_succ from the tree
		if node_succ.is_node_leaf():
			node_succ.disconnect_node_from_parent()
		else:
			self.bst_delete_has_one_child(node_succ)
		# replace node by node_succ
		if self.root == node:
			self.root = node_succ
			node_succ.set_parent(None)
		else:
			node_parent = node.get_parent()
			node_succ.set_parent(node_parent)
			if node_parent.get_right() == node:
				node_parent.set_right(node_succ)
			else:
				node_parent.set_left(node_succ)
		# Set parent of sons after switch
		node_succ.set_left(node.get_left())
		if node.get_left().is_real_node():
			node.get_left().set_parent(node_succ)
		node_succ.set_right(node.get_right())
		if node.get_right().is_real_node():
			node.get_right().set_parent(node_succ)
		node.set_parent(None)
		node.set_left(AVLNode(None, None))
		node.set_right(AVLNode(None, None))
		return parent


	def bst_delete(self, node: AVLNode) -> AVLNode:
		"""
		Performs a delete operation on a node in a Binary Search tree and returns the parent of the physically deleted node.
		:param node: The node we want to delete.
		:return: Parent of the physically deleted node.
		"""
		# print(f"Deleting node {node}")
		# print(f"parent - {node.get_parent()}, left - {node.get_left()}, right - {node.get_right()}")
		# print(f"delete, tree is {self}")
		parent = node.get_parent()
		# First we handle node is leaf.
		if node.is_node_leaf():
			if self.root == node:
				# Case where node is also root.
				self.root = None
			else:
				node.disconnect_node_from_parent()
		# Second we handle node has only one real child.
		elif node.get_left().is_real_node() ^ node.get_right().is_real_node():
			self.bst_delete_has_one_child(node)
		# Last we handle node has 2 real children
		else:
			parent = self.bst_delete_has_twins(node)
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
		# Then we create the first subtrees
		left_tree = AVLTree(node.get_left())
		if node.get_left().is_real_node():
			node.get_left().disconnect_node_from_parent()
		right_tree = AVLTree(node.get_right())
		if node.get_right().is_real_node():
			node.get_right().disconnect_node_from_parent()
		# Create the rest of T1
		for small_tree_node in left_tree_nodes[0:]:
			sub_tree_left = small_tree_node.get_left()
			small_tree_node.get_left().disconnect_node_from_parent()
			left_tree.join(tree2=AVLTree(sub_tree_left), key=small_tree_node.get_key(),
						   val=small_tree_node.get_value())
		# Create the rest of T2
		for big_tree_node in right_tree_nodes[0:]:
			sub_tree_right = big_tree_node.get_right()
			big_tree_node.get_right().disconnect_node_from_parent()
			right_tree.join(tree2=AVLTree(sub_tree_right), key=big_tree_node.get_key(),
							val=big_tree_node.get_value())
		trees_list = [left_tree, right_tree]
		return trees_list

	def join(self, tree2: AVLTree, key: int, val) -> int:
		"""
		joins self with key and another AVLTree
		@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
		:param tree2: a dictionary to be joined with self
		:param key: The key separating self with tree2
		:param val: The value attached to key
		:return: the absolute value of the difference between the height of the AVL trees joined
		"""
		# checking special cases (one or both trees are None)
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

		# both trees have root
		else:
			current_tree_height = self.get_root().get_height()
			tree2_height = tree2.get_root().get_height()
			heights_difference = current_tree_height - tree2_height
			middle_node = AVLNode(key, val)

			# find out which tree is with bigger keys
			if self.get_root().get_key() > middle_node.get_key():
				self.choose_order_and_connect(tree2.get_root(), middle_node, self.get_root())
			else:
				self.choose_order_and_connect(self.get_root(), middle_node, tree2.get_root())
			return 1 + abs(heights_difference)


	def choose_order_and_connect(self, smaller_tree_root, middle_node, bigger_tree_root):
		"""
		the method receive the trees and the node received in join after checking which of them has bigger keys
		the method compare the height of the trees and then send the taller tree to a method that find a subtree with
		the other tree height.
		then the method send the subtree that has been found, the other tree and the node that should be their parents
		to a method that connect them
		if the trees have the same height it's automatically send them to the method that connect them.


		@param smaller_tree_root: the root of the tree from the given trees in join with smaller keys
		@param middle_node: the node that connect the trees given in join
		@param bigger_tree_root: the root of the tree from the given trees in join with bigger keys
		@return:
		"""
		smaller_tree_height = smaller_tree_root.get_height()
		bigger_tree_height = bigger_tree_root.get_height()

		if smaller_tree_height > bigger_tree_height:
			subtree_of_taller_tree_root = (self.get_pointer_to_appropriate_subtree_with_specific_height
										   (smaller_tree_root,bigger_tree_height, True))
			self.connect_trees(bigger_tree_root, middle_node, subtree_of_taller_tree_root)

			if subtree_of_taller_tree_root == smaller_tree_root :
				self.root = middle_node
			else:
				self.root = smaller_tree_root

		elif smaller_tree_height < bigger_tree_height:
			subtree_of_taller_tree_root = (self.get_pointer_to_appropriate_subtree_with_specific_height
										   (bigger_tree_root, smaller_tree_height, False))
			self.connect_trees(subtree_of_taller_tree_root, middle_node, smaller_tree_root)

			if subtree_of_taller_tree_root == bigger_tree_root :
				self.root = middle_node
			else:
				self.root = bigger_tree_root

		else:
			self.connect_trees(bigger_tree_root, middle_node, smaller_tree_root)
			self.root = middle_node

		self.maintain_tree_balance(middle_node)

	def get_pointer_to_appropriate_subtree_with_specific_height(self, tree_root, requested_height, smaller):
		# complexity analysis: the method going down to a leaf, by that it does at most log(n) actions, every action cost
		# O(1) and hence the complexity is O(log(n))

		"""
		the method searching for an appropriate node from the tallest tree between the trees that received in join:
		if the taller one is the bigger tree the method return the subtree with same height as the smaller tree.
		the root of the subtree is the smallest node with this height in the taller tree.
		if the taller one is the smaller tree the method return the subtree with same height as the bigger tree.
		the root of the subtree is the biggest node with this height in the taller tree. if the node isn't real,
		the method return his father
		@param tree_root: the root of the tallest tree between the trees that received in join
		@param requested_height: the height of the lowest tree between the trees that received in join
		@param smaller: True if the root belong to the biggest tree between the trees that received in join or the
		smallest one
		@return: a pointer to an appropriate subtree of the taller tree between the trees received in join. if the
		taller one is the bigger tree the method return the subtree with same height as the smaller tree. the root of the
		subtree is the smallest node with this height in the taller tree. if the
		taller one is the smaller tree the method return the subtree with same height as the bigger tree. the root of the
		subtree is the biggest node with this height in the taller tree. if the node isn't real, the method return his father
		"""
		tmp_pointer = tree_root

		if not smaller:
			while tmp_pointer.get_height() > requested_height and tmp_pointer.get_left().is_real_node():
				tmp_pointer = tmp_pointer.get_left()

		else:
			while tmp_pointer.get_height() > requested_height and tmp_pointer.get_right().is_real_node():
				tmp_pointer = tmp_pointer.get_right()

		if not tmp_pointer.is_real_node():
				tmp_pointer = tmp_pointer.get_parent()

		return tmp_pointer

	def connect_trees(self, bigger_tree_root, middle_node, smaller_tree_root):
		"""
		Connects a subtree of the taller tree with the node that received in join and the shorter tree
		than, the method connects the tree that created by the connection to the rest of the taller tree
		@param smaller_tree_root: the root of the tree from the given trees in join with smaller keys
		@param middle_node: the node that connect the trees given in join
		@param bigger_tree_root: the root of the tree from the given trees in join with bigger keys
		@return:
		"""
		# problem might be here if smaller_tree_root or bigger_tree_root are None
		if smaller_tree_root is None or bigger_tree_root is None:
			logging.warning("----------- assigning None to sons-------------")
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
