class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = newdata

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

        if self.head.get_next() == None:
            self.tail = temp

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def search(self,item):
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found: # assumes item exists
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None: # item is head
            self.head = current.get_next()
        else:
            if current.get_next() == None: # item is tail
                self.tail = previous

            previous.set_next(current.get_next())

    def append(self, item):
        temp = Node(item)
        self.tail.set_next(temp)
        self.tail = temp


class OrderedList:
    def __init__(self):
        self.head = None
