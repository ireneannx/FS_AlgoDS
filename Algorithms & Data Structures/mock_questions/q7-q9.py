"""Q7 Implement the Vigenere Cipher
Although the idea of the Vigenere Cipher is very basic it took humanity over 300 years to break it.
Ultimately, frequency analysis broke it. Develop the class to encrypt and decrypt using the cipher developed by
Vigenere."""

"""Q8 Calculate the frequency of items in a given sequence
Given a sequence of elements (that support equality function), calculate the frequency of each distinct element. 
For example, given the sequence [‘hi’, ‘I’, ‘am’, ‘Alexa’, ‘I’, ‘would’, ‘just’, ‘like’, ‘to’, ‘say’, ‘hi’]. 
The output should be:
"""


class StringList:
    dict = {}

    @staticmethod
    def calculate_freq(list_):
        for i in range(len(list_)):
            count = 1
            if list_[i] in StringList.dict.keys():
                continue
            for j in range(i + 1, len(list_)):

                if list_[i] == list_[j]:
                    count += 1

            StringList.dict[list_[i]] = count

        return StringList.dict


# ans = StringList.calculate_freq(['hi', 'hello', 'i', 'am', 'tired', 'hi', 'i', 'tried', 'hi'])
# print(ans)

"""
Find two numbers in a sequence to add up to a given number
Given a sequence of numbers find any two numbers that add up to another given number. For example, given the sequence 
[3, 4, 1, 7 , 9, 17] and the number 8, the solution is [1, 7], because these two add up to 8."""


def find_sum(list_, num):
    for i in range(len(list_)):
        for j in range(i+1, len(list_)):
            if list_[i] + list_[j] == num:
                print(f'{list_[i]} and {list_[j]} add up to {num}')
                arr = [list_[i], list_[j]]
                return arr

    print('none found')
    return 0


y = find_sum([3, 4, 1, 7, 9, 17], 8)
print(y)
