import pandas as pd

def return_index(list_, person):
    for i in range(len(list_)):
        if list_[i] == person:
            return i
    Exception('index out of range!!!!!!')
class Person:
    def __init__(self, name):
        self.name = name
        self.preference = None
        self.partner = None

    def __str__(self): 
        # for petinting nodes easily
        # s = self.name self.partner}'
        return str(self.name)

    def set_preference(self, list_of_persons):  # make into dict later
        self.preference = list_of_persons

    def show_preferences(self):
        """
        just prints out a persons preferences 
        """
        for pref in self.preference:
            print(pref)
        
        return 0 

    def make_proposal(self):
        preferences = self.preference
        for pref in preferences:
            if pref is not None:
                next_choice = pref

                self.choose(next_choice) 
                break
    
        return 0

    def choose(self, girl):

        if girl.partner is None:
            girl.partner = self
            self.partner = girl
        else:
            current_guy = girl.partner
            # loop through girls preference list to see which guy is better
            preferences = girl.preference
            current_guy_index = return_index(preferences, current_guy)
            potential_guy_index = return_index(preferences, self)
            print(current_guy_index, potential_guy_index)
            

            if potential_guy_index > current_guy_index:
                print(f'sorry, {self} has been rejected by {girl}')
            #     remove girl from guys list
                girl_index = return_index(self.preference, girl)
                self.preference[girl_index] = None
            else:
                print(f'congratulations! {self} has been accepted by {girl}')
                # remove girl from prev guys list 
                girl_index = return_index(current_guy.preference, girl)
                current_guy.preference[girl_index] = None
                current_guy.partner = None 

                # set girl up with new guy 
                self.partner = girl
                girl.partner = self


        return 0


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

# def choose(girl, potential_guy):
#     if girl.partner is None:
#         girl.partner = potential_guy
#         potential_guy.partner = girl
#     else:
#         current_guy = girl.partner
#         # loop through girls preference list to see which guy is better
#         preferences = girl.preference
#         current_guy_index = return_index(preferences, current_guy)
#         potential_guy_index = return_index(preferences, potential_guy)
#         print(current_guy_index, potential_guy_index)
        

#         if potential_guy_index > current_guy_index:
#             print(f'sorry, {potential_guy} has been rejected by {girl}')
#         #     remove girl from guys list
#             girl_index = return_index(potential_guy.preference, girl)
#             potential_guy.preference[girl_index] = None
#         else:
#             print(f'congratulations! {potential_guy} has been accepted by {girl}')
#             # remove girl from prev guys list 
#             girl_index = return_index(current_guy.preference, girl)
#             print(f'ex index = {girl_index}')
#             current_guy.preference[girl_index] = None
#             current_guy.partner = None 

#             # set girl up with new guy 
#             potential_guy.partner = girl
#             girl.partner = potential_guy


#     return 0



# def make_proposal(person):
#     preferences = person.preference
#     for pref in preferences:
#         if pref is not None:
#             next_choice = pref
#             choose(next_choice, person)
#             break
    
#     return 0



proposers = [a,b,c]
acceptors = [A,B,C]

choices = 3 #num of preferences for everyone

for choice in range(choices):
    for i in range(len(proposers)):
        if(proposers[i].partner is None):
            proposers[i].make_proposal()
    

    # check if all engaged
for proposer in proposers:
    print (f'({proposer}, {proposer.partner})')

