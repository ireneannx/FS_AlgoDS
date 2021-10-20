"""
Given a list of pairs of synonyms and a sentence, return all possible synonymous sentences. Below is an example.
Input:

synonyms = [["happy","joyful"],["sad","sorrow"],["joyful","cheerful"]],
sentence = "I am happy today but was sad yesterday
Output:
["I am cheerful today but was sad yesterday",
"I am cheerful today but was sorrow yesterday",
"I am happy today but was sad yesterday",
"I am happy today but was sorrow yesterday",
"I am joyful today but was sad yesterday",
"I am joyful today but was sorrow yesterday"]
Please note that joyful is a synonym of happy and since cheerful is a synonym of joyful, cheerful is consequently a
synonym of happy. This is reflected in the output of the example above.
"""


def separate_synonyms(sentence, synonyms):
    arr = sentence.split()
    dict = {}

    # put words from sentence which have available synonyms in dictionary
    for elem in arr:
        for pair in synonyms:
            if elem in pair and elem not in dict.keys():
                dict.setdefault(elem, [])

    # print(dict.values())

    for key in dict.keys():

        for pair in synonyms:
            if key in pair:
                dict[key].append(pair[0])
                dict[key].append(pair[1])

    print(dict.values())
    values = dict.values()
    print(type(values))
#     separate synonyms


#     look for dict keys in synonyms
#     rows = len(synonyms)
#     columns = 2
#
#     for i in range(rows): #in each row
#         #we look at both columns for the key
#         for j in range(columns):
#             if synonyms(i,j) in dict.keys():
#                 #add all values in row to the dict values


sentence = "I am happy today but was sad yesterday"
synonyms = [["happy", "joyful"], ["sad", "sorrow"], ["joyful", "cheerful"]]
separate_synonyms(sentence, synonyms)
