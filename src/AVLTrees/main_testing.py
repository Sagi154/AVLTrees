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
    print(f"tree before inserting {node1} ")
    print(bst)
    rots1 = bst.insert(*node1)
    print(f"tree after inserting {node1} ")
    print(bst)
    print(f"tree before inserting {node2} ")
    print(bst)
    rots2 = bst.insert(*node2)
    print(f"tree after inserting {node2} with {rots2} rotations")
    print(bst)
    print(f"tree before inserting {node3} ")
    print(bst)
    rots3 = bst.insert(*node3)
    print(f"tree after inserting {node3} ")
    print(bst)
    print(f"tree before inserting {node4} ")
    print(bst)
    rots4 = bst.insert(*node4)
    print(f"tree after inserting {node4} ")
    print(bst)

    bst.insert(19,"asdf")
    bst.insert(5,"asdf")
    bst.insert(83,"asdf")
    bst.insert(2,"asdf")
    bst.insert(9,"asdf")
    bst.insert(1,"asdf")
    print(bst)


    print("begin exp")
    A = AVLTree(AVLNode(9 , "asd"))
    B = AVLTree(AVLNode(19, "asd"))

    B.insert(17, "asd")
    B.insert(83, "asd")

    print(A)
    print(B)


    A.join(B,13, "asd")

    print(A)
    print("the end is here")


    node = bst.search(9)
    print(node)
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

