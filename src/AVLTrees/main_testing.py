from avl_template import *
from logs_config import set_log_config


def main():
    set_log_config()
    print("Started Testing AVL")
    root = AVLNode(6, "asd")
    bst = AVLTree(root)
    node1 = (8, 'asdf')
    node2 = (7, 'asf')
    node3 = (13, 'asf')
    node4 = (17, 'asf')
    rots1 = bst.insert(*node1)
    rots2 = bst.insert(*node2)
    rots3 = bst.insert(*node3)
    rots4 = bst.insert(*node4)

    bst.insert(19,"asdf")
    bst.insert(5,"asdf")
    bst.insert(83,"asdf")
    bst.insert(2,"asdf")
    bst.insert(9,"asdf")
    bst.insert(1,"asdf")
    print("------testing split on tree-------")
    print(bst)
    node = bst.search(8)
    print(f"node to be tested is {node.get_key()}")
    lst = bst.split(node)
    print(f"Tree left {lst[0]}")
    print(f"Tree right {lst[1]}")
    # node = bst.search(17)
    # print(f"tree before deleting {node} ")
    # print(bst)
    # bst.delete(node)
    # print(f"tree after deleting {node} ")
    # print(bst)
    #
    # node2 = bst.search(6)
    # print(f"tree before deleting {node2} ")
    # print(bst)
    # bst.delete(node2)
    # print(f"tree after deleting {node2} ")
    # print(bst)


if __name__ == "__main__":
    main()

