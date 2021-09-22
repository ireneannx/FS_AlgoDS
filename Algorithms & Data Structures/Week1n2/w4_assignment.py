# google style guide for python PEP8 and PEP20
# Object oriented programing
# create a linked list
import random as rd
from time import perf_counter_ns
import pandas as pd


class Node:
    # this is every data point on the linked list
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, nodes=None):
        # we need to know where the list starts
        self.head = None

        # to create a linked list easily
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:  # index 0 already popped so elem starts from next index
                node.next = Node(data=elem)
                node = node.next

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

    def add_to_beginning(self, node):
        node.next = self.head
        self.head = node

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

        if self.head is None:
            raise Exception("List is empty")
        elif index == 0:
            self.head = self.head.next
            return

        previous_node = self.at(index - 1)
        next_node = self.at(index + 1)
        previous_node.next = next_node
        return

    def at(self, index):  # searching
        i = 0

        if self.head is None:
            raise Exception("List is empty")

        for current_node in self:
            if i == index:
                return current_node
            i += 1

        raise Exception('index given is too large. Length of linked list is shorter than index given')


# llist = LinkedList(['a', 'r', 'q', 'i', 'r', 'e'])

# llist.add_to_end(Node('d'))
# print(llist)
#
# llist.insert(0, Node('pls work'))
# print(llist)
# print(len(llist))
# llist.remove(0)
# print(llist)


# print(llist.at(3))

# for i in llist: #this wont work without iter func
#     print(i)

# creating a linked list of 1000 elements
def list_generation(number_entries: int):
    """
        Generates a randomly ordered list of a certain length
        :param number_entries: The length of the list
        :return: randomly ordered list
    """
    # Create an randomly ordered list
    array = list(range(number_entries))
    # Randomly shuffle the list
    rd.shuffle(array)
    return array


def main():
    sizes = [1000, 2000, 4000, 8000, 16000, 32000]
    time_array = []
    df = pd.DataFrame(columns=['sizes', 'time_average'])

    for i in range(len(sizes)):
        # Generate list and sort
        random_list = list_generation(sizes[i])

        llist = LinkedList(random_list)

        # calculating time for adding to a list
        start_time = perf_counter_ns()
        llist.add_to_beginning(Node('start'))
        end_time = perf_counter_ns()

        time_taken = end_time - start_time
        print(time_taken)
        time_array.append(time_taken)

    #    add values to df
    i = 0
    for size in sizes:
        df.loc[i, 'sizes'] = size
        df.loc[i, 'time_average'] = time_array[i]
        i += 1

    print(df)


main()
