import math
import logging
from AVLTree import *
from logs_config import set_log_config
import random
from pprint import pprint

def perform_theoretical_test(square: int):
    size = int(1000 * math.pow(2, square))
    print(f"-------Size of tree {size}------------")
    tree1, tree2 = random_test(size)
    random_key = random.randint(1, size)
    random_node = tree1.search(random_key)
    max_node = AVLTree.max(tree2.get_root().get_left())
    costs1 = tree1.split(random_node)[1]
    print(f"Split for random node:{random_key} :\n Avg cost of join: {costs1[0]} \n Max cost of join: {costs1[1]}")
    costs2 = tree2.split(max_node)[1]
    print(f"Split for max node in left sub tree:{max_node.get_key()}:\n Avg cost of join: {costs2[0]} \n Max cost of join: {costs2[1]}")
    return costs1, costs2

def perform_test():
    sum_of_random_split_avg_costs = 0
    sum_of_random_split_max_cost = 0
    sum_of_det_split_avg_costs = 0
    sum_of_det_split_max_cost = 0
    num_of_tests = 5
    for i in range(10):
        print(f"======================================= Started tests for i: {i + 1} =======================================")
        for j in range(num_of_tests):
            print(f"--------------------- Starting test #{j+1} for i: {i+1} -----------------------")
            costs_random, costs_max = perform_theoretical_test(i+1)
            sum_of_random_split_avg_costs += costs_random[0]
            sum_of_random_split_max_cost += costs_random[1]
            sum_of_det_split_avg_costs += costs_max[0]
            sum_of_det_split_max_cost += costs_max[1]
        print(f"======================================= Ended tests for i: {i+1} =======================================")
        print(f"Split for random node: :\n Avg cost of join: {sum_of_random_split_avg_costs/num_of_tests} \n Max cost of join: {sum_of_random_split_max_cost/num_of_tests}")
        print(f"Split for max node in left sub tree:\n Avg cost of join: {sum_of_det_split_avg_costs/num_of_tests} \n Max cost of join: {sum_of_det_split_max_cost/num_of_tests}")
        sum_of_random_split_avg_costs = 0
        sum_of_random_split_max_cost = 0
        sum_of_det_split_avg_costs = 0
        sum_of_det_split_max_cost = 0



def random_test(keys_count: int):
    tree1 = AVLTree()
    tree2 = AVLTree()
    RANGE_OF_KEYS = keys_count
    NUMBER_OF_METHOD_calls = math.floor(RANGE_OF_KEYS * random.random())
    NUMBER_OF_METHOD_calls = RANGE_OF_KEYS
    print(NUMBER_OF_METHOD_calls)
    array_for_testing = [0 for i in range(RANGE_OF_KEYS + 1)]
    count = 0
    key = random.randint(1, RANGE_OF_KEYS)
    while count < NUMBER_OF_METHOD_calls:
        key = random.randint(1, RANGE_OF_KEYS)
        if array_for_testing[key] == 0:
            count += 1
            array_for_testing[key] = 1
            tree1.insert(key, 0)
            tree2.insert(key, 0)
    # print(bst.get_root().get_size())
    # node = bst.get_root()
    # for i in range(node.get_height()):
    #     print(f"------------Level: {i}---------------")
    #     print(f"node: {node}")
    #     print(f"Left {node.get_left()} \n Right {node.get_right()}")
    #     # if node.get_size() < 50:
    #     #     print(AVLTree(node))
    #     node = node.get_right()
    return tree1, tree2

def determined_test(keys_count: int) -> AVLTree:
    print(f"---------called for determined test with {keys_count}-----")
    NUMBER_OF_KEYS = keys_count
    bst = AVLTree()
    for i in range(NUMBER_OF_KEYS):
    # for i in range(random.randint(1, NUMBER_OF_KEYS)):
        logging.debug(f"\n before inserting {i+1} tree is \n {bst}")
        b_ops = bst.insert(i + 1, 0)
        logging.debug(f"\n inserted {i}, rotations: {b_ops} \n tree is \n {bst}")
    root = bst.get_root()
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


def test_cases_split():
    tree = AVLTree()
    tree.insert(8,0)   #problematic
    # tree.insert(9, 0)
    # tree.insert(10, 0)
    node = tree.search(8)
    logging.warning(f"\n before split, tree: \n {tree}")
    ret = tree.split(node)
    logging.warning(f"\n split for {node} \n ret is \n{ret[0]} \n{ret[1]}")


def test_some_case_in_join():
    tree1 = AVLTree()
    tree1.insert(10, 0)
    tree1.insert(7, 0)
    tree1.insert(12, 0)
    tree1.insert(6, 0)
    tree1.insert(8, 0)
    tree1.insert(11, 0)
    tree1.insert(5, 0)

    tree2 = AVLTree()
    tree2.insert(30, 0)
    tree2.insert(26, 0)
    tree2.insert(35, 0)
    tree2.insert(25, 0)
    tree2.insert(27, 0)
    tree2.insert(34, 0)
    tree2.insert(36, 0)

    print(tree1)
    print(tree2)

    tree1.join(tree2, 15, 0)
    print(tree1)


def test_another_case_of_join():
    tree1 = AVLTree()
    tree2 = AVLTree()
    tree1.insert(20, 0)
    logging.debug(f"\n {tree1}")
    logging.debug(f"\n {tree2}")
    tree2.join(tree1, 25, 0)
    logging.debug(f"\n {tree2}")





def main():
    set_log_config()
    test_another_case_of_join()
    # test_some_case_in_join()
    # test_cases_split()
    # perform_test()
    # tree, tree1 = random_test(100)
    # test_join()
    # test_ops_count_from_forum()
    # test_split()
    # tree = determined_test(10)
    # node = tree.search(7)
    # print(node)
    # tree.split(node)
    # print(tree.avl_to_array())
    # determined_test(1000)
    # test()


if __name__ == "__main__":
    main()
