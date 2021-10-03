# google style guide for python PEP8 and PEP20
# Object oriented programing
# create a linked list
import random as rd
from time import perf_counter_ns
import pandas as pd
import matplotlib.pyplot as plt


class Node:
    # this is every data point on the linked list
    def __init__(self, data):
        self._data = data
        self._next = None  # where the node points to -> another node

    def __str__(self):
        return str(self.data)  # for printing node(s) easily

    @property
    # getter func
    def data(self):
        print('in getter')
        return self._data

    @data.setter
    def data(self, new):
        self._data = new

    @property
    # getter func
    def next(self):
        return self._next

    @next.setter
    def next(self, new_nxt):

        if isinstance(new_nxt, Node) or new_nxt is None:
            self._next = new_nxt
        else:
            raise TypeError


class LinkedList:
    def __init__(self, nodes=None) -> object:
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
        connector = ' '
        for i in range(len(self)):
            if i > 0:
                connector += '->'
            connector += f'{node.data}'
            node = node.next

        return connector

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

    def add_to_end(self, data):
        """
        a function to insert a new node at the end of the linked list
        :param data: the new data to be inserted
        :return: None
        """
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        # traverse whole list till you reach the end
        for current_node in self:
            pass

        # now current_node is at the last element. current_node still in the function scope
        current_node.next = node

    def add_to_beginning(self, data):
        """
        a function to add a new node to the beginning of the list
        :param data: the new data to be inserted
        :return: None
        """
        node = Node(data)
        node.next = self.head
        self.head = node

        return

    def insert(self, index, data):  # inserting between 2 nodes, at the position specified by index
        """
        function inserts a new node (data) at the index specified in the linked list
        :param index: the index the new node should be at
        :param data: the data to be inserted
        :return: None
        """
        i = 0

        node = Node(data)

        if self.head is None:
            self.add_to_beginning(self, data)
            return
        elif index == 0:
            node.next = self.head
            self.head = node
            return
        else:
            previous_node = self.at(index)
            next_node = previous_node.next

            #     switch links
            previous_node.next = node
            node.next = next_node
            return

        # in case index given is larger than length of list
        print('index given is too large. Length of linked list is shorter than index given')
        return

    def remove(self, index):  # remove a node. make sure the elements before n after deleted node are still connected

        """
        function to remove the node at the imdex specified
        :param index: index of the node to be removed
        :return: none
        """

        if self.head is None:
            raise Exception("List is empty")
        elif index == 0:
            self.head = self.head.next
        else:
            previous_node = self.at(index - 1)
            next_node = self.at(index + 1)
            previous_node.next = next_node

        return

    def at(self, index):  # searching
        """
        function to search for the data value at the index specified in the linked list
        :param index: index at which you want to retrieve data
        :return: the node at the index specified
        """
        i = 0

        if self.head is None:
            raise Exception("List is empty")

        for current_node in self:
            if i == index:
                return current_node
            i += 1

        raise Exception('index given is out of range. Length of linked list is shorter than index given')


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


def plot_creator(df: pd.DataFrame):
    """
    Creates plot out of the DataFrame with array length on x-axis and duration in seconds on y axis
    :param df: DataFrame containing array length and duration of respective insertion sort
    :return: none
    """
    # Define the plot
    plt.style.use("bmh")
    fig, ax = plt.subplots()
    ax.plot(df["sizes"], df["time_average"], label="adding to linked list", marker="o", linestyle="-")

    # Prepare the labels and title
    ax.legend(loc="upper left")
    ax.set_xlabel("Linked list length")
    ax.set_ylabel("Duration in nanoseconds")
    ax.set_title("Time complexity of adding a new element in a linked list")

    # Create plot and save it
    plt.show()
    # fig.savefig("assignment1_insertion_sort_time_complexity/figure_assigment_1")


def main():
    sizes = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000]
    time_array = []
    df = pd.DataFrame(columns=['sizes', 'time_average'])

    for i in range(len(sizes)):
        # Generate list and sort
        random_list = list_generation(sizes[i])

        llist = LinkedList(random_list)

        # calculating time for adding to a list
        thing = 'start'
        start_time = perf_counter_ns()
        llist.add_to_beginning(thing)
        end_time = perf_counter_ns()

        time_taken = end_time - start_time

        time_array.append(time_taken)

    #    add values to df
    i = 0
    for size in sizes:
        df.loc[i, 'sizes'] = size
        df.loc[i, 'time_average'] = time_array[i]
        i += 1

    print(df)

    #   plot
    plot_creator(df)


main()

# comments
# why is the time complexity not 0(n)
# need to implement time complexity for searching --> at func
