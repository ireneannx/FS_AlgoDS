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

    def __iter__(self): #to make object iterable
        node = self.head
        # result = []
        while node is not None:
            # result.append(node)
            yield node
            node = node.next

        # return result
    def add_to_end(self, node): #starting at the head. add is insert at the end
        if self.head is None:
            self.head = node
            return

      # traverse whole list till you reach the end
        for current_node in self:
            pass

    # now current_node is at the last element. current_node still in the function scope
        current_node.next = node



    # def at(self, index): #if youre at the fiest half start at the head, 2nd half start at tail
    #     ''''''
    # def insert(self, index, data): #insert a node
    #     ''''''
    # def remove(self, index): #remove a node. make sure the elements before n after deleted node are still connected
    #     ''''''
    # def __len__(self): #len of list
    #     ''''''


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

# for i in llist: #this wont work without iter func
#     print(i)

