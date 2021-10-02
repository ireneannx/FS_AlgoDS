import pandas as pd


class Person:
    def __init__(self, name):
        self.name = name
        self.preference = None
        # self.status = 0 #engaged(1) or single(0)
        self.partner = None

    def __str__(self):
        return str(self.name)  # for printing node(s) easily

    def set_preference(self, list_of_persons):  # make into dict later
        self.preference = list_of_persons


# proposers a,b,c
# acceptors A,B,C

# proposers initialisation
a = Person('a')
b = Person('b')
c = Person('c')

# acceptors initialisatiom
A = Person('A')
B = Person('B')
C = Person('C')

# proposers pref
prefa = [A, B, C]

prefb = [B, A, C]

prefc = [A, C, B]

# acceptors pref
prefB = [a, b, c]

prefC = [b, a, c]

prefA = [c, b, a]

# set preferences for proposers
a.set_preference(prefa)
b.set_preference(prefb)
c.set_preference(prefc)

# set preferences for acceptors
A.set_preference(prefA)
B.set_preference(prefB)
C.set_preference(prefA)


# print(A.preference[1])


def return_index(list_, guy):
    for i in range(len(list_)):
        if list_[i] == guy:
            return i
    Exception('index out of range!!!!!!')


def choose(girl, potential_guy):
    if girl.partner is None:
        girl.partner = potential_guy
        potential_guy.partner = girl
    else:
        current_guy = girl.partner
        # loop through girls preference list to see which guy is better
        preferences = girl.preference
        current_guy_index = return_index(preferences, current_guy)
        potential_guy_index = return_index(preferences, potential_guy)
        print(current_guy_index, potential_guy_index)

        if current_guy_index > potential_guy_index:
            print(f'sorry, {potential_guy} has been rejected by {girl}')
        #     remove girl from guys list
        else:
            print()


        return 0


#
def propose(guy):
    preferences = guy.preference
    preferred_girl = preferences[0]
    choose(preferred_girl, guy)
    return 0


choose(A, b)
choose(A, c)
