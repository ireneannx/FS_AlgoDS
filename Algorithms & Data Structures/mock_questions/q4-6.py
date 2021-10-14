#Q4 Determine if a sequence of numbers is increasing
# Given a sequence of numbers, determine if each element is larger than the previous element.

x = [1,2,3,4,5,5,7,8,9]

def is_increasing(seq):

  for i in range(len(seq) - 1):
    if seq[i + 1] <= seq[i]:
      print('This is not an increasing sequence')
      return 0

  print('This is an increasing sequence.')
  return 1

is_increasing(x)

# Determine the longest sequence of increasing numbers in a list of number
# Given a sequence of numbers, determine the longest streak of consecutive numbers that are increasing. For example given the sequence [1, 2, 5, 3, 8, 9, 13, 24, 21], the longest sequence is [3, 8, 9, 13, 24].

def longest_sequence(seq):
  max = []
  for i in range(len(seq)):
    for j in range(i+1, len(seq)):
      if seq[i] < seq[j] and is_increasing(seq[i:j+1]):
          new = seq[i:j+1]
          if len(new)>len(max):
            max = new  
  return max

print (longest_sequence([1, 2, 5, 3, 8, 9, 13, 24, 21]))

# Determine given two strings if one is an anagram of the other
# Given two strings, determine if one is an anagram of the other. For example, the two strings “anagram” and “margana” are anagrams of each other.