# Q4 Determine if a sequence of numbers is increasing
# Given a sequence of numbers, determine if each element is larger than the previous element.

x = [1, 2, 3, 4, 5, 5, 7, 8, 9]


def is_increasing(seq):
    for i in range(len(seq) - 1):
        if seq[i + 1] <= seq[i]:
            print('This is not an increasing sequence')
            return 0

    print('This is an increasing sequence.')
    return 1


# is_increasing(x)


# Q5 Determine the longest sequence of increasing numbers in a list of number
# Given a sequence of numbers, determine the longest streak of consecutive numbers that are increasing.
# For example given the sequence [1, 2, 5, 3, 8, 9, 13, 24, 21], the longest sequence is [3, 8, 9, 13, 24].

def longest_sequence(seq):
    max = []
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] < seq[j] and is_increasing(seq[i:j + 1]):
                new = seq[i:j + 1]
                if len(new) > len(max):
                    max = new
    return max


# print(longest_sequence([1, 2, 5, 3, 8, 9, 13, 24, 21]))


#Q6 Determine given two strings if one is an anagram of the other
# Given two strings, determine if one is an anagram of the other. For example, the two strings “anagram” and “margana”
# are anagrams of each other.

def is_anagram(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 == len2:
        for i in range(len1):
            if str1[i] != str2[len1-i-1]:
                print('not anagram')
                return 0

        print('its an anagram!')
        return 1
    else:
        print('different lengths, not anagram')
        return 0

is_anagram('anagram','margana')

'''
we will need to iterate 'forwards' through the length of the first string (after checking if both strings are of equal length)
from i = 0 to i = length - 1, and check if the element at the i-th index of the first string is equal to the length of 
(the length -1 -i)th index of the second string. The -1 is because string indexing starts from 0 in python. 
If the check fails, we immediately know that the string is not an anagram and we can return 0 for "not anagram".
Otherwise, if the loop completes successfully, we can return 1 for 'is anagram'

Since this program needs to loop through a constant O(1) block n times in the worst case (i.e if it is indeed an anagram)
the time complexity will be O(n). 
'''

