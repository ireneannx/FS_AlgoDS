"""
Given a list of lists (matrix) where every row (list) is sorted in strictly increasing order
(i.e. there are no duplicates), return the smallest common element in all rows. If there is no common element, return -1
Below is an example. Input:
"""


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


def find_common_elem(mat):
    n_rows = len(mat)

    long_list = sum(mat, [])

    # we sort long_list using merge sort
    sorted_list = divide_merge(long_list)
    print(sorted_list)
    # first element to repeat the same number of times as there are rows MUST appear in all lists and has to
    # be the minimum

    count = 1
    last_elem = None
    for i in range(len(sorted_list)):
        if sorted_list[i] == last_elem:
            count += 1
            last_elem = sorted_list[i]
        else:
            count = 1
            last_elem = sorted_list[i]

        if count == n_rows:
            print(f'found it! : {sorted_list[i]}')
            return sorted_list[i]

    #     if no such element exists
    return -1


mat = [[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]
mat2 = [[3, 4, 6, 7, 14, 15, 16], [1, 3, 4, 5, 10, 14, 20], [2, 3, 5, 7, 11, 14, 19], [1, 3, 7, 9, 12, 13, 14]]
find_common_elem(mat2)

"""Exam Outline:
Detailed description of approach with explanation:

To find the minimum repeated element in the list of list we first combine the list into one long list of all
elements. We then sort this list using the merge sort algorithm in ascending order. 

to do -> describe the merge sort algo (lets call this the sorted list)

Since there are no duplicate numbers in each row in the matrix, if we loop through the sorted list and find the first 
element that repeats the same number or times as there are rows in the matrix then we know that that particular element 
must be the minimum value that appears in every single row. 

Steps:
1) construct a long list from list of lists
2) sort it in ascending order
3) loop through the list to find if any element appears the same number of times as there are rows in the main matrix
    a) if such an element exists, return this element and exit the function
    
4) if no matching element was found in 3) which matches the criteria, then return -1


Downside: this function will not work if any list in the list of lists have repeating elements

Time Complexity - O(n) + O(nlogn) = O(n)
TODO : explain time complexity 
"""
