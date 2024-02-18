from AVLTree import *
from logs_config import set_log_config
import random
from pprint import pprint


def random_test(keys_count: int):
    bst = AVLTree()
    RANGE_OF_KEYS = keys_count
    NUMBER_OF_METHOD_calls = RANGE_OF_KEYS
    array_for_testing = [0 for i in range(RANGE_OF_KEYS + 1)]
    count = 0
    key = random.randint(1, RANGE_OF_KEYS)
    while count < NUMBER_OF_METHOD_calls:
        key = random.randint(1, RANGE_OF_KEYS)
        if array_for_testing[key] == 0:
            count += 1
            array_for_testing[key] = 1
            bst.insert(key, 0)
    print(bst.get_root().get_size())
    node = bst.get_root()
    for i in range(node.get_height()):
        print(f"------------Level: {i}---------------")
        print(f"node: {node}")
        print(f"Left {node.get_left()} \n Right {node.get_right()}")
        # if node.get_size() < 50:
        #     print(AVLTree(node))
        node = node.get_right()
    return bst


def determined_test(keys_count: int) -> AVLTree:
    print(f"---------called for determined test with {keys_count}-----")
    NUMBER_OF_KEYS = keys_count
    bst = AVLTree()
    for i in range(NUMBER_OF_KEYS):
        logging.info(f"\n before inserting {i} tree is \n {bst}")
        b_ops = bst.insert(i, 0)
        logging.info(f"\n inserted {i}, rotations: {b_ops} \n tree is \n {bst}")
    root = bst.get_root()
    print(root)
    return bst

def test():
    tree = AVLTree()
    rotations = tree.insert(8, 8)
    logging.info(f"\n inserted 8, rotations: {rotations} \n tree is \n {tree}")
    rotations = tree.insert(7, 7)
    logging.info(f"\n inserted 7, rotations: {rotations} \n tree is \n {tree}")
    rotations = tree.insert(6, 6)
    logging.info(f"\n inserted 6, rotations: {rotations} \n tree is \n {tree}")
    rotations = tree.insert(5, 5)
    logging.info(f"\n inserted 5, rotations: {rotations} \n tree is \n {tree}")
    node = tree.search(5)
    rotations = tree.delete(node)
    logging.info(f"\n deleted 5, rotations: {rotations} \n tree is \n {tree}")
    node = tree.search(6)
    rotations = tree.delete(node)
    logging.info(f"\n deleted 6, rotations: {rotations} \n tree is \n {tree}")

def test_join():
    logging.warning(f"\n Testing join")
    tree1 = AVLTree()
    tree2 = AVLTree()

    tree1.insert(2, 0)
    tree1.insert(6, 0)
    tree1.insert(4, 0)
    tree1.insert(3, 0)
    tree1.insert(9, 0)
    node = tree1.search(9)
    logging.warning(f"\n test successor for node 9 {tree1.successor(node)}")
    node = (20, 0)
    tree2.insert(24, 0)
    tree2.insert(29, 0)
    tree2.insert(25, 0)
    tree2.insert(22, 0)
    tree2.insert(21, 0)
    tree2.insert(39, 0)
    tree2.insert(41, 0)
    tree2.insert(31, 0)
    tree2.insert(27, 0)
    logging.warning(f"\n first tree is {tree1}")
    logging.warning(f"\n second tree is {tree2}")
    logging.warning(f"\n join cost is {tree1.join(tree2, *node)} and tree is \n {tree1}")

def test_split():
    tree = AVLTree()
    tree.insert(25, 0)
    tree.insert(9, 0)
    tree.insert(33, 0)

    tree.insert(5, 0)
    tree.insert(13, 0)
    tree.insert(29, 0)
    tree.insert(59, 0)

    tree.insert(2, 0)
    tree.insert(11, 0)
    tree.insert(20, 0)
    tree.insert(31, 0)

    tree.insert(10, 0)
    tree.insert(18, 0)
    tree.insert(23, 0)
    logging.warning(f"\n tree test for split is {tree}")
    node = tree.search(23)
    left, right = tree.split(node)
    logging.warning(f"\n left tree is \n {left} \n right tree is \n {right}")
    logging.warning(f"\n left root is {left.get_root()} \n right root is {right.get_root()}")

def test_ops_count_from_forum():
    tree = AVLTree()
    arr = [15, 22, 8, 24, 4, 20, 11, 18, 9, 12, 2, 13]
    for k in arr:
        tree.insert(k, 0)
    print(tree)
    node = tree.search(11)
    print(tree.delete(node))
    print(tree)

def main():
    set_log_config()
    tree = random_test(25)
    # test_join()
    # test_ops_count_from_forum()
    # test_split()
    # tree = determined_test(30)
    print(tree)
    # print(tree.avl_to_array())
    # determined_test(1000)
    # test()


if __name__ == "__main__":
    main()
