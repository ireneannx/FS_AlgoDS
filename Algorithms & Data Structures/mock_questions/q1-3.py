# Determine if a given string is a palindrome
# A palindrome is sequence that reads same backwards as forwards. “Anna”, for example is a palindrome. The task is to determine if a given string is a palindrome.


def isPalindrome():
  x = input('Type in a string')
  length = len(x)
  n_times = int(length/2)

  # check if forwards = backwards 
  for i in range(n_times):
    if x[i] != x[length - 1 - i]:
      print('Not a palindrom')
      return 0 

  print(f'{x} is a palindrome!')
  return 0 

isPalindrome()

# Find all palindromic sections of any given string longer than one
# A palindrome is a sequence that reads the same backwards as forwards. “Anna”, for example is a palindrome. The task is to find all palindromic sequences within any given string. The word “intellect” for example includes following palindromic sections:
# “ll” intel​ l​ect
# “elle” inte​ lle​ct

