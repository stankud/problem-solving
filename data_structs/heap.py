class BinHeap():
    """
    [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]

                   5
            9            11
       14      18     19    21
     33  17  27

    1
    2
    4
    8
    16
    32
    64
    128
    """


    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    ### PUBLIC ###

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size += 1

        self._percolate_up(self.current_size)

    def del_min(self):
        root_index = 1
        min = self.heap_list[root_index]

        self.heap_list[root_index] = self.heap_list.pop()
        self.current_size -= 1

        self._percolate_down(root_index)

        return min

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]

        while (i > 0):
            self._percolate_down(i)

            i = i - 1

    ### PRIVATE ###
    def _get_parent(self, child):
        return child // 2

    def _percolate_up(self, child):
        hl = self.heap_list
        parent = self._get_parent(child)

        if hl[child] < hl[parent]:
            tmp = hl[parent]
            hl[parent] = hl[child]
            hl[child] = tmp

            self._percolate_up(parent)

    def _min_child(self, parent):
        hl = self.heap_list
        lchild = parent * 2
        rchild = parent * 2 + 1

        if rchild > self.current_size:
            return lchild

        if hl[lchild] < hl[rchild]:
            min_child = lchild
        else:
            min_child = rchild

        return min_child

    def _percolate_down(self, parent):
        hl = self.heap_list
        min_child = self._min_child(parent)

        if min_child <= self.current_size and hl[min_child] < hl[parent]:
            tmp = hl[parent]
            hl[parent] = hl[min_child]
            hl[min_child] = tmp

            self._percolate_down(min_child)
