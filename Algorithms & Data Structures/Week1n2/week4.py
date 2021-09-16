# OOP

class Student:
    def __init__(self, first_name, last_name):  # dunder func
        self.first_name = first_name
        self.last_name = last_name

    #   a function for changing attribute
    def set_last_name(self, last_name):
        self.last_name = last_name

    def __str__(self):  # another dunder obj
        return self.first_name + " " + self.last_name

    def __lt__(self, other): #lt means lesser than
        return self.__str__().upper < other.__st__().upper()


#     for dunder funcs (predefined) you dont need to call it as kilian.__str__(), u can just use str(kilian) notation
#     dunder funcs r great because it makes your code easier to read

kilian = Student('Kilian', 'Veruegen')
vahe = Student('Vahe', "Andonians")

print(kilian)
# to change an attribute

# method 1
kilian.set_last_name(
    "Veruegen1")  # method 1 is preferred over method 2 is SE. Ideally you shuld only try to change parts
#                                 of a class WITHIN that class
# method 2
kilian.last_name = 'Verweyen'
# print(kilian.last_name)

# the coolness of dunder functions
print(kilian.__str__())
print(str(kilian))  # more readable so use this. thanks to dunder functions
print(kilian)  # this works too because the print func automatically looks for str

#
new_list  = [vahe, kilian]
print(str(new_list[0]))
