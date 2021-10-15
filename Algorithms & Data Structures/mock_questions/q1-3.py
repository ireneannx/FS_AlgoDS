# Q1 Determine if a given string is a palindrome
# A palindrome is sequence that reads same backwards as forwards. “Anna”, for example is a palindrome. The task is to determine if a given string is a palindrome.


def isPalindrome(x):
    length = len(x)
    n_times = int(length / 2)

    # check if forwards = backwards
    for i in range(n_times):
        if x[i] != x[length - 1 - i]:
            print('Not a palindrom')
            return 0

    print(f'{x} is a palindrome!')
    return 1

    # time complexity : O(n)


# x = input('Type in a string: ')
# isPalindrome(x)
# -----------------------------------------------------------------------

# Q3 Print out all Fibonacci numbers smaller or equal to a given number
# Given a positive number, print out all Fibonacci numbers smaller or equal to that number. For example, given the number 11 the program should print out: 1 1 2 3 5 8
# The next Fibonacci number would be 13 which is already larger than 11.

def print_fibonacci(num):
    a = 1
    b = 1
    c = 1
    while True:
        print(c)
        c = a + b
        a = b
        b = c

        if (c > num):
            return 0
# time complexity = O(n)
# print_fibonacci(24)

# using recursion
# this function has crazy time complexity. for every number, it recalculates the fibonnaci.
# to counter we use memoization.
def fibonacci(num):
    if num == 0:
        return num
    elif num <= 2:
        return 1
    else:
        return fibonacci(num - 2) + fibonacci(num - 1)


# better func
memory = {}

def fibonacci2(num):
    if num == 0:
        return num
    elif num <= 2:
        return 1
    elif num in memory.keys():
        return memory[num]
    else:
        f = fibonacci(num - 2) + fibonacci(num - 1)
        memory[num] = f
        return f

# problem = in this func we are using a variable (memory) that is ourside the func
# to solve, use OOP

class Fibonacci:
    m = {}

    @staticmethod
    def get(n):
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        elif n in Fibonacci.m.keys():
            return Fibonacci.m[n]
        else:
            f = Fibonacci.get(n-1) + Fibonacci.get(n-2)
            Fibonacci.m[n] = f
            return f

print(Fibonacci.get(100))

def find_largest_fibonacci(x):
    n = 0
    while True:
        f = fibonacci(n)
        if f>x:
            break
        n += 1
    return fibonacci2(n-1)





# -----------------------------------------------------------------------

# Q2 Find all palindromic sections of any given string longer than one
# A palindrome is a sequence that reads the same backwards as forwards. “Anna”, for example is a palindrome. The task is to find all palindromic sequences within any given string. The word “intellect” for example includes following palindromic sections:
# “ll” 
# “elle” 

def how_many_palindromes(x):
    # first we go to the part where the same alphabet repeats twice
    words = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] == x[j]:
                # words next to each other
                if j == i + 1:
                    words.append(x[i:j + 1])
                else:
                    # words farther off. check if words between are a palindrome
                    y = x[i: j + 1]
                    if isPalindrome(y):
                        words.append(y)

        print(words)

# x = input('Type a string: ')
# how_many_palindromes(x)
# -----------------------------------------------------------------------
