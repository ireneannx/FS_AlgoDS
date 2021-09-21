# google style guide for python PEP8 and PEP20
# Object oriented programing
# create a linked list

class Node:
    # this is every data point on the linked list
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        # we need to know where the list starts
        self.head = None
        ...

    def __str__(self):  # to loop thru n show some kinda separator so u can see output easily
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")

        return "->".join(nodes)

    def __iter__(self):  # to make object iterable
        node = self.head
        # result = []
        while node is not None:
            # result.append(node)
            yield node
            node = node.next

        # return result

    def __len__(self):  # returns len of list
        count = 0
        node = self.head

        while node is not None:
            count += 1
            node = node.next

        return count

    def add_to_end(self, node):  # starting at the head. add is insert at the end
        if self.head is None:
            self.head = node
            return

        # traverse whole list till you reach the end
        for current_node in self:
            pass

        # now current_node is at the last element. current_node still in the function scope
        current_node.next = node

    def insert(self, index, data):  # inserting between 2 nodes, at the position specified by index
        i = 0

        if self.head is None:
            print('Linked List is empty. Use Add function instead')
            return
        elif index == 0:
            data.next = self.head
            self.head = data
            return

        for current_node in self:

            if i == index - 1:
                data.next = current_node.next
                current_node.next = data
                return
            i += 1

        # in case index given is larger than length of list
        print('index given is too large. Length of linked list is shorter than index given')
        return

    def remove(self, index):  # remove a node. make sure the elements before n after deleted node are still connected
        i = 0

        if self.head is None:
            raise Exception("List is empty")
        elif index == 0:
            self.head = self.head.next

        for current_node in self:

            if i == index - 1:
                to_delete = current_node.next
                next_node = to_delete.next
                current_node.next = next_node
                return

            i += 1

    def at(self, index):  # searching
        i = 0

        if self.head is None:
            raise Exception("List is empty")

        for current_node in self:
            if i == index:
                return current_node
            i += 1

        raise Exception('index given is too large. Length of linked list is shorter than index given')

llist = LinkedList()

first = Node('a')
second = Node('b')
third = Node('c')
llist.head = first
first.next = second
second.next = third

print(llist)
llist.add_to_end(Node('d'))
print(llist)

llist.insert(0, Node('pls work'))
print(llist)
print(len(llist))
# llist.remove(1)
# print(llist)
print(llist.at(7))

# for i in llist: #this wont work without iter func
#     print(i)
