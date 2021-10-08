import pandas as pd


class Person:
    def __init__(self, name):
        self.name = name
        self.preference = None
        # self.status = 0 #engaged(1) or single(0)
        self.partner = None

    def __str__(self): 
        # for petinting nodes easily
        # s = self.name self.partner}'
        return str(self.name)

    
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




def return_index(list_, person):
    for i in range(len(list_)):
        if list_[i] == person:
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
        girl_index = return_index(current_guy.preference, girl)

        if potential_guy_index > current_guy_index:
            print(f'sorry, {potential_guy} has been rejected by {girl}')
        #     remove girl from guys list
            potential_guy.preference[girl_index] = None
        else:
            print(f'congratulations! {potential_guy} has been accepted by {girl}')
            # remove girl from prev guys list 
            print(f'ex index = {girl_index}')
            current_guy.preference[girl_index] = None
            current_guy.partner = None 

            # set girl up with new guy 
            potential_guy.partner = girl
            girl.partner = potential_guy


    return 0


#
# def make_proposal(boy):
#     preferences = person.preference
#     next_choice = preferences[0]
#     choose(next_choice, boy)
#     return 0



print(A)
print(a)
choose(A, a)
print(f'{A} partner-{A.partner} pref-{A.preference}')
# print(f'{a} partner-{a.partner} pref-{a.preference}')
choose(B,b)
choose(A,c)
print(f'{A} partner-{A.partner} pref-{A.preference}')
print(C.partner)
print(f'{a} partner-{a.partner} pref-{a.preference}')


