import math
import time
from utils import make_rand_list

def min_num_1(num_list):
    start = time.time()
    list_len = len(num_list)
    min_num = None

    for i in num_list:
        for j_idx, j in enumerate(num_list):
            if i > j:
                break
            elif j_idx == list_len -1: # if looped reached the last element
                return i, time.time() - start

num_list_1 = make_rand_list(10000000)

print('\nSOLUTION 1: 𝑂(𝑛2)\n')

for i in range(5):
    print("Min number is %d required %10.7f seconds" % min_num_1(num_list_1))

def min_num_2(num_list):
    start = time.time()
    min_num = math.inf

    for i in num_list:
        if i < min_num:
            min_num = i

    return min_num, time.time() - start

print('\nSOLUTION 2: 𝑂(𝑛)\n')

for i in range(5):
    print("Min number is %d required %10.7f seconds" % min_num_2(num_list_1))
