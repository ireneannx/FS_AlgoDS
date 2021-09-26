# ------------------------------------ CREATING A BALANCED BINARY SEARCH TREE
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

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

    def get(self, key):
        if self.key == key:
            print(self.data)
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
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
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
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __str__(self):
        s = f"{self.key} : {self.value} \n"
        return s


def sort_list(num):
    # use merge sort to sort an unsorted list in the future
    # for now im just creating a sorted list
    list = []
    for i in range(num):
        val = "Amy" + str(i)
        key = i
        list.append(KeyValue(key, val))

    return list


list = sort_list(10)

nodes = []


def node_list(list):
    sorted_list = list
    length = len(sorted_list)
    mid_index = length // 2
    mid_key = list[mid_index].key

    nodes.append(mid_key)

    left = sorted_list[:mid_index]
    right = sorted_list[mid_index + 1:]
    if len(left) > 1:
        node_list(left)
    else:
        nodes.append(left[0].key)

    if len(right) > 1:
        node_list(right)
    elif len(right) == 1:
        nodes.append(right[0].key)

    return nodes


def create_balanced_binary_search_tree(list):
    # sorted_list = merge_sort(list_)
    sorted_list = list
    nodes = node_list(sorted_list)

    # generate balanced binary search tree
    i = 0
    for node_index in nodes:
        if i == 0:
            root = Node(sorted_list[node_index].key, sorted_list[node_index].value)
        else:
            root.insert(sorted_list[node_index].key, sorted_list[node_index].value)

        i += 1

    return root


root = create_balanced_binary_search_tree(list)

root.display()
