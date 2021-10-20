# ------------------------------------ CREATING A SELF BALANCING BINARY SEARCH TREE - AVL TREE
# (for left-left and right-right cases)

"""__author__ = "Irene"
__email__ = "irene.iype@fs-students.de,"""


# the merge sort functions


def divide_merge(array):
    """
    Splits arrays into lists of size 1 recursively. Then sorts from the lowest level up through the sort() function.
    :param array: unsorted array
    :return: a sorted array (through sort function)
    """

    if len(array) <= 1:
        return array

    # divide array into 2 lists
    split_point = len(array) // 2
    list_1 = array[:split_point]
    list_2 = array[split_point:]

    # split recursively until len(arrray) = 1. Then sends to sort function
    sorted_list_1 = divide_merge(list_1)
    sorted_list_2 = divide_merge(list_2)

    return sort(sorted_list_1, sorted_list_2)


def sort(array1, array2):
    """
    Sorts two sorted arrays
    :param array1: the first sorted array
    :param array2: the second sorted array
    :return: a new sorted array
    """

    sorted_array = []

    while 0 < len(array1) and 0 < len(array2):
        # comparing first element. The smaller of the two elements appended to sorted_array until one array is empty
        if array1[0] > array2[0]:
            sorted_array.append(array2.pop(0))
        else:
            sorted_array.append(array1.pop(0))

    # the non-empty array from the previous step gets added to sorted_array
    if 0 < len(array1):
        sorted_array.extend(array1)
    elif 0 < len(array2):
        sorted_array.extend(array2)

    return sorted_array


# merge sort function end----------

# every node in the BST is of class Node
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.balance_factor = None

    def __str__(self):
        s = f"Key: {self.key} , Value: {self.data} \n"
        return s

    # functions for calculating balance factor -------------

    def get_height(self):
        """
        returns height of current node. For one-None tree, height is 1.
        """
        if self.left is None:
            left_height = 0
        else:
            left_height = self.left.get_height()

        if self.right is None:
            right_height = 0
        else:
            right_height = self.right.get_height()

        if self.right is None and self.left is None:
            return 1
        else:
            height = 1 + max(left_height, right_height)
            return height

    def get_height_in_class(self):

        if self.right is None and self.left is None:
            return 1

        left_height = 0
        if self.left is not None:
            left_height = self.left.get_height_in_class()

        right_height = 0
        if self.right is not None:
            right_height = self.right.get_height_in_class()

        return max(left_height, right_height) + 1

    def get_balance_factor(self):

        """
        calculates the balance factor of self/node and assigns it to self.balance factor
        returns the balance factor
        """

        if self.left is None:
            left_height = 0
        else:
            left_height = self.left.get_height()

        if self.right is None:
            right_height = 0
        else:
            right_height = self.right.get_height()

        self.balance_factor = right_height - left_height

        return self.balance_factor

    def fill_balance_factor(self):
        self.get_balance_factor()

        # no child
        if self.right is None and self.left is None:
            return 0
            # Only left child
        elif self.right is None:
            self.left.fill_balance_factor()

        # only right child
        elif self.left is None:
            self.right.fill_balance_factor()

        # both children
        else:
            self.right.fill_balance_factor()
            self.left.fill_balance_factor()

    # -----------------

    # rotate functions so tree becomes an AVL tree

    def right_rotate(self):  # for left left case
        x = self  # parent of pivot
        y = self.left  # pivot point
        z = y.left  # left child of pivot (rotation point)

        y.left = z.right
        z.right = y
        x.left = z

        return

    def left_rotate(self):  # for right right case
        x = self
        y = self.right
        z = y.right

        y.right = z.left
        z.left = y
        x.right = z

        return

    def insert(self, key, data):

        if self.key == key:
            # override the data
            self.data = data
        elif key > self.key:  # go right

            # check if right is none!!!!
            if self.right is None:
                self.right = Node(key, data)
            else:
                # insert data
                self.right.insert(key, data)  # this works
                # self.insert(self, self.right) ---> this wont work because youre calling insert on current self instead
                # of calling it on self.right. self.right becomes the new self

        else:  # go left, do the same

            if self.left is None:
                self.left = Node(key, data)
            else:
                self.left.insert(key, data)

        # to make tree self balancing, we need to calculate balance factor after insertion. if BF<-1 => left rotate, BF >1 = right rotate

        if self.left and abs(self.left.get_balance_factor()) > 1:
            # left left case
            if (
                    self.left.get_balance_factor() == -2 and self.left.left.get_balance_factor() == -1):  # accessing the pivot parent
                # do right rotate
                print(' -> left left case')
                self.right_rotate()

        if self.right and abs(self.right.get_balance_factor()) > 1:
            # right right case
            if (
                    self.right.get_balance_factor() == 2 and self.right.right.get_balance_factor() == 1):  # accessing the pivot parent
                # do left rotate
                print(' -> right right case')
                self.left_rotate()

    def get(self, key):
        if self.key == key:
            # print(self.data)
            return self.data
        elif key > self.key:  # go right
            # check if right is none!!!!
            if self.right is None:
                Exception("not found")
                return 0
            else:
                return self.right.get(key)  # ---> this works

            # else return self.get(self.right.key) #---> why wont this work? because self.get is calling the get
            # function where you currently are. self.right is calling the get function for self.right
        else:  # go left
            if self.left is None:
                print("not found")
                return 0
            else:
                return self.left.get(key)

    # function to display binary search tree -from Vahe ---------------------
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""

        # getting balance factor so we can add it to the tree later
        self.get_balance_factor()

        # No child.
        if self.right is None and self.left is None:
            line = '%s (%s)' % (self.key, self.balance_factor)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s (%s)' % (self.key, self.balance_factor)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s (%s)' % (self.key, self.balance_factor)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s (%s)' % (self.key, self.balance_factor)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class KeyValue:

    # each element/node to be inserted into the BST is a KeyValue class

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __str__(self):
        s = f"{self.key} : {self.value} \n"
        return s


def create_balanced_binary_search_tree(list) -> object:
    """
    function to create balanced binary search tree
    :param list: random list of keyvalue pairs to be create the tree
    :return: root node of balanced binary search tree
    """
    # sort the list using merge sort
    sorted_list = divide_merge(list)

    if len(sorted_list) == 0:
        return None

    mid = len(sorted_list) // 2
    mid_root = Node(sorted_list[mid].key, sorted_list[mid].value)
    mid_root.left = create_balanced_binary_search_tree(sorted_list[:mid])
    mid_root.right = create_balanced_binary_search_tree(sorted_list[mid + 1:])

    return mid_root


# creating a balanced binary search tree end----------

if __name__ == '__main__':
    root = create_balanced_binary_search_tree(
        [KeyValue(13, 13), KeyValue(15, 15), KeyValue(16, 16), KeyValue(10, 10), KeyValue(11, 11), KeyValue(8, 8),
         KeyValue(5, 5), KeyValue(4, 4)])

    root.display()

    print('Example of left left case: ')
    root.insert(3, 3)
    root.display()

    print('Example of right right case: ')
    root.insert(17, 17)
    root.insert(18, 18)
    root.display()
