import random
import math

def make_rand_list(el_count):
    rand_list = []
    for i in range(0, el_count):
        num = math.ceil(random.random() * el_count * 10)
        rand_list.append(num)

    return rand_list
