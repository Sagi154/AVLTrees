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


def determined_test(keys_count: int):
    print(f"---------called for determined test with {keys_count}-----")
    NUMBER_OF_KEYS = keys_count
    bst = AVLTree()
    for i in range(NUMBER_OF_KEYS):
        logging.info(f"\n before inserting {i} tree is \n {bst}")
        b_ops = bst.insert(i, 0)
        logging.info(f"\n inserted {i}, rotations: {b_ops} \n tree is \n {bst}")
    root = bst.get_root()
    print(root)
    # print(bst)

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


def main():
    set_log_config()
    # random_test(200)
    determined_test(30)
    # determined_test(1000)
    # test()

    # print("----------Test join seperately---------")
    # bst2 = AVLTree(None)
    # bst2.insert(250, 0)
    # node = 200, 0
    # tree2 = AVLTree(None)
    # tree2.insert(130, 0)
    # tree2.insert(45, 0)
    # print(f"bst2 is {bst2}")
    # print(f"node is: {node}")
    # print(f"tree2 is {tree2}")
    # bst2.join(tree2, *node)


if __name__ == "__main__":
    main()
