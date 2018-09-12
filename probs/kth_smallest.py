import time
from utils import make_rand_list
from math import inf
from data_structs.heap import BinHeap

num_list_1 = make_rand_list(1000000)
num_list_3 = make_rand_list(10000000)

def find_kth_smallest1(num_list, k):
    start = time.time()
    prev_min = -inf

    i = 0
    while i < k:
        j = 0
        curr_min = inf
        while j < len(num_list):
            if num_list[j] > prev_min and num_list[j] < curr_min:
                curr_min = num_list[j]

            j += 1
        prev_min = curr_min
        i += 1

    return curr_min, time.time() - start

num_list_2 = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
num_list_2.reverse()


def find_kth_smallest2(num_list, k):
    start = time.time()
    bh = BinHeap()

    # for el in num_list:
        # bh.insert(el)

    bh.build_heap(num_list)

    i = 0
    while i < k:
        min_num = bh.del_min()
        i += 1

    return min_num, time.time() - start

print("find_kth_smallest1(): %d required %10.7f seconds" % find_kth_smallest1(
    num_list_1, 82))
print("find_kth_smallest2(): %d required %10.7f seconds" % find_kth_smallest2(
    num_list_1, 82))
