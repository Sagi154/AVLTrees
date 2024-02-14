from AVLTree import *
from logs_config import set_log_config


def main():
    set_log_config()
    bst = AVLTree(None)

    # bst.insert(293, 0)
    # bst.insert(200, 0)
    # bst.insert(130, 0)
    # bst.insert(450, 0)
    # bst.insert(45, 0)
    # bst.insert(250, 0)
    # bst.insert(260, 0)
    # node = bst.search(260)
    # bst.split(node)
    # print(bst.search(293))
    # print(bst.search(100))
    # print(bst)



    print("----------Test join seperately---------")
    bst2 = AVLTree(None)
    bst2.insert(250, 0)
    node = 200, 0
    tree2 = AVLTree(None)
    tree2.insert(130, 0)
    tree2.insert(45, 0)
    print(f"bst2 is {bst2}")
    print(f"node is: {node}")
    print(f"tree2 is {tree2}")
    bst2.join(tree2, *node)


    # print("Started Testing AVL")
    # print("begin exp")
    # A = AVLTree(AVLNode(9 , "asd"))
    # B = AVLTree(AVLNode(19, "asd"))
    #
    # B.insert(17, "asd")
    # B.insert(83, "asd")
    #
    # print(A)
    # print(B)
    #
    #
    # A.join(B,13, "asd")
    #
    # print(A)
    # print("the end is here")
    #
    # root = AVLNode(6, "asd")
    # bst = AVLTree(root)
    # node1 = (8, 'asdf')
    # node2 = (7, 'asf')
    # node3 = (13, 'asf')
    # node4 = (17, 'asf')
    # rots1 = bst.insert(*node1)
    # rots2 = bst.insert(*node2)
    # rots3 = bst.insert(*node3)
    # rots4 = bst.insert(*node4)
    # bst.insert(19, "asdf")
    # bst.insert(5, "asdf")
    # bst.insert(83, "asdf")
    # bst.insert(2, "asdf")
    # bst.insert(9, "asdf")
    # bst.insert(1, "asdf")
    # print("------testing split on tree-------")
    # print(bst)
    #
    # node = bst.search(9)
    # print(node)
    # node = bst.search(8)
    # print(f"node to be tested is {node.get_key()}")
    # lst = bst.split(node)
    # print(f"Tree left {lst[0]}")
    # print(f"Tree right {lst[1]}")

if __name__ == "__main__":
    main()

