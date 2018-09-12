from data_structs.list import UnorderedList

ul = UnorderedList()

ul.add(17)
ul.add(8)
ul.add(10)

ul.append(88)

ul.add(33)

ul.append(75)

current = ul.head
while current:
    print(current.data)

    current = current.get_next()

print('head', ul.head.data)
print('tail', ul.tail.data)

ul.remove(75)

current = ul.head
while current:
    print(current.data)

    current = current.get_next()

print('head', ul.head.data)
print('tail', ul.tail.data)
