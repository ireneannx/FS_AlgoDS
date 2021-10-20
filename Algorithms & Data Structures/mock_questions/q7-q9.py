"""Q7 Implement the Vigenere Cipher
Although the idea of the Vigenere Cipher is very basic it took humanity over 300 years to break it.
Ultimately, frequency analysis broke it. Develop the class to encrypt and decrypt using the cipher developed by
Vigenere."""


# this works for a capitals only plaintext
class VignereCipher:


    @staticmethod
    def generate_key(plaintext, keyword):
        n_key = list(keyword)
        if len(plaintext) == len(n_key):
            return "".join(n_key)
        else:
            for i in range(len(plaintext) - len(n_key)):
                n_key.append(n_key[i])

        return "".join(n_key)

    @staticmethod
    def encrypt(plaintext, keyword):
        key = VignereCipher.generate_key(plaintext, keyword)
        cipher_text = []
        for i in range(len(plaintext)):
            x = (ord(plaintext[i].upper()) +
                 ord(key[i])) % 26  # get 'extra', remainder
            x += ord('A')
            cipher_text.append(chr(x))

        return ''.join(cipher_text)

    @staticmethod
    def decrypt(encrypted_text, keyword):

        key = VignereCipher.generate_key(encrypted_text, keyword)
        orig_text = []
        for i in range(len(encrypted_text)):
            x = (ord(encrypted_text[i]) -
                 ord(key[i])+26) % 26
            x += ord('A')
            orig_text.append(chr(x))

        return "".join(orig_text)


trial = VignereCipher.encrypt('hello', 'aoy')
trial2 = VignereCipher.decrypt('OYPSI','aoy')

print(trial)
print(trial2)
"""Q8 Calculate the frequency of items in a given sequence
Given a sequence of elements (that support equality function), calculate the frequency of each distinct element. 
For example, given the sequence [‘hi’, ‘I’, ‘am’, ‘Alexa’, ‘I’, ‘would’, ‘just’, ‘like’, ‘to’, ‘say’, ‘hi’]. 
The output should be:"""


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
            for j in range(i + 1, len(list_)):
                if list_[i] + list_[j] == num:
                    print(f'{list_[i]} and {list_[j]} add up to {num}')
                    arr = [list_[i], list_[j]]
                    return arr

        print('none found')
        return 0

    # y = find_sum([3, 4, 1, 7, 9, 17], 8)
    # print(y)

"""
Exam Outline:
Detailed description of approach with explanation:
Data structures used: list, dict, etc
Comments on implementation: downsides, inefficiencies, room for improvement, not handled edge cases
Time complexity: 
"""
