# gale shapely as implemented in class
# you can tell a function in python what type you are expecting

class Proposer:
    def __init__(self, name):
        self.name = name
        # self.preferences = None
        # self.match = None
        # self.proposal_index = 0

    def set_preferences(self, preferences):
        self.preferences = preferences
        self.match = None
        self.proposal_index = 0

    def propose(self):
        if self.match is not None:
            return
        if self.proposal_index >= len(self.preferences):
            raise Exception(f'{self.name} ran out of preferences to propose to')
            # exception is a class predefined by python. It takes in the string error message
        self.match = self.preferences[self.proposal_index].receive(self)
        self.proposal_index += 1  # move to the next proposer if you get dumped

    def dump(self):
        # if proposer got dumped
        self.match = None
        # self.proposal_index += 1

    def matched(self):
        return self.match is not None


class Receiver:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def set_preferences(self, preferences):
        self.preferences = {}
        i = 0
        while i < len(preferences):  # use enumerate() here
            self.preferences[preferences[i].name] = i  # dict_name[key] = value
            i += 1
        self.match = None

    def receive(self, proposer):
        if proposer.name not in self.preferences:
            raise Exception(f'{self.name} does not know {proposer.name}')

        if self.match is None:
            self.match = proposer
            return self

        elif self.preferences[proposer.name] < self.preferences[self.match.name]:
            # if proposer is better than the current guy
            self.match.dump()  # dumb current match
            self.match = proposer  # get engaged to new proposer
            return self

        else:
            return None  # proposer got rejected


a = Proposer('A')
b = Proposer('B')
c = Proposer('C')
d = Proposer('D')
e = Proposer('E')

l = Receiver('L')
n = Receiver('N')
m = Receiver('M')
o = Receiver('O')
p = Receiver('P')

a.set_preferences([o, m, n, l, p])
b.set_preferences([p, n, m, l, p])
c.set_preferences([m, p, l, o, n])
d.set_preferences([p, m, o, n, l])
e.set_preferences([o, l, m, n, p])

l.set_preferences([d, b, e, c, a])
m.set_preferences([b, a, d, c, e])
n.set_preferences([a, c, e, d, b])
o.set_preferences([d, a, c, b, e])
p.set_preferences([b, e, a, c, d])

proposers = [a, b, c, d, e]
receivers = [l, m, n, o, p]


def make_match(proposers):
    all_matched = False
    while not all_matched:

        for proposer in proposers:
            # if proposer.match is None: -> dont do this. leave the logic to the object
            proposer.propose()

        all_matched = True
        for p in proposers:
            all_matched = all_matched and p.matched()
            if not all_matched:
                break


make_match(proposers)

for p in proposers:
    print(f'{p.name},{p.match.name}')
