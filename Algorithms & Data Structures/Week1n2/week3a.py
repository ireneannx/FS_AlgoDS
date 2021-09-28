import random as rd
from time import perf_counter_ns


def merge_sort(array):
    start_time = perf_counter_ns()
    divide_merge(array)
    end_time = perf_counter_ns()
    return len(array), end_time - start_time, array


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


# ----------- all functions before this is for merge sort

class Student:
    def __init__(self, first_name, last_name):  # dunder func
        self.first_name = first_name
        self.last_name = last_name

    #   a function for changing attribute
    def set_last_name(self, last_name):
        self.last_name = last_name

    def __str__(self):  # another dunder obj
        return self.first_name + " " + self.last_name

    def __lt__(self, other):
        # lt means lesser than, it shows what the sign < means anytime an object in this class is used for comparison
        if self.last_name.upper() == other.last_name.upper():
            'then compare first names'
            return self.first_name.upper() < other.first_name.upper()
        else:
            'else compare last names'
            return self.last_name.upper() < other.last_name.upper()

    # not necessary to write __gt__ since its understood from the lt dunder func.
    def __gt__(self, other):
        if self.last_name.upper() == other.last_name.upper():
            'then compare first names'
            return self.first_name.upper() > other.first_name.upper()
        else:
            'else compare last names'
            return self.last_name.upper() > other.last_name.upper()


kilian = Student('Kilian', 'Veruegen')
vahe = Student('Vahe', "Andonians")
xander = Student('Xander', "Andonians")
irene = Student("irene", "iype")
kiran = Student("kiran", "iype")
jasmin = Student('jasmin', "capka")
anthony = Student('Anthony', 'Ang')

# y = kilian < vahe
# print(y) --> returns false

new_list = [vahe, kilian, irene, jasmin, anthony, kiran, xander]

sorted = divide_merge(new_list)

for i in range(len(sorted)):
    print(sorted[i])
