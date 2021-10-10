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
Adam = Person('Adam')
Bill = Person('Bill')
Carl = Person('Carl')
Dan = Person('Dan')
Eric = Person('Eric')

# acceptors initialisatiom
Amy = Person('Amy')
Beth = Person('Beth')
Cara = Person('Cara')
Diane = Person('Diane')
Ellen = Person('Ellen')

# set preferences for acceptors
Amy.set_preference([Eric, Adam, Bill, Dan, Carl])
Beth.set_preference([Carl, Bill, Dan, Adam, Eric])
Cara.set_preference([Bill, Carl, Dan, Eric, Adam])
Diane.set_preference([Adam, Eric, Dan, Carl, Bill])
Ellen.set_preference([Dan, Bill, Eric, Carl, Adam])

# set preferences for proposers
Adam.set_preference([Beth, Amy, Diane, Ellen, Cara])
Bill.set_preference([Diane, Beth, Amy, Cara, Ellen])
Carl.set_preference([Beth, Ellen, Cara, Diane, Amy])
Dan.set_preference([Amy, Diane, Cara, Beth, Ellen])
Eric.set_preference([Beth, Diane, Amy, Ellen, Cara])

proposers = [Adam, Bill, Carl, Dan, Eric]
acceptors = [Amy, Beth, Cara, Diane, Ellen]

choices = len(proposers) #num of preferences for everyone = len(proposers)

def gale_shapely(proposers):

    while True: #for each choice 
        exit = 0 
        for i in range(len(proposers)): #go through each proposer
            if(proposers[i].partner is None):
                proposers[i].make_proposal()
                exit += 1 
        
        #exit early if all engaged 
        if exit == 0:
            break

    # print matches
    for proposer in proposers:
        print (f'({proposer}, {proposer.partner})')

gale_shapely(proposers)
