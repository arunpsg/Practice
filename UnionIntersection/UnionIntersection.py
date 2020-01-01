class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def isPresent(llist, value):
    cur_node = llist.head
    while cur_node:
        if cur_node.value is value:
            return True
        else:
            cur_node = cur_node.next
    return False


def union(llist_1, llist_2):
    # Your Solution Here

    unionLl = LinkedList()

    node1 = llist_1.head
    while node1:
        unionLl.append(node1.value)
        node1 = node1.next
    node2 = llist_2.head
    while node2:
        if not isPresent(unionLl, node2.value):
            unionLl.append(node2.value)
        node2 = node2.next
    return unionLl


def intersection(llist_1, llist_2):
    # Your Solution Here

    intersectionll = LinkedList()
    # node1 = llist_1.head
    node2 = llist_2.head
    while node2:
        # while node2:
        #     if node2.value is node1.value:
        #         intersectionll.append(node2.value)
        #     node2 = node2.next
        if isPresent(llist_1, node2.value):
            intersectionll.append(node2.value)
        node2 = node2.next
    return intersectionll


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

#Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
