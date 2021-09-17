# making a binary search tree class

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):

        if self.key == key:
            # override the data
            self.data = data
        elif key > self.key:  # go right

            # check if right is none!!!!
            if self.right is None:
                self.right = Node(key, data)
            else:
                # insert data
                self.right.insert(key, data)  # this works
                # self.insert(self, self.right) ---> this wont work because youre calling insert on current self instead
                # of calling it on self.right. self.right becomes the new self

        else:  # go left, do the same

            if self.left is None:
                self.left = Node(key, data)
            else:
                self.left.insert(key,data)

    def get(self, key):
        if self.key == key:
            print(self.data)
            return self.data
        elif key > self.key:  # go right
            # check if right is none!!!!
            if self.right is None:
                print("not found")
                return 0
            else:
                return self.right.get(key)  # ---> this works

            # else return self.get(self.right.key) #---> why wont this work? because self.get is calling the get
            # function where you currently are. self.right is calling the get function for self.right
        else:  # go left
            if self.left is None:
                print("not found")
                return 0
            else:
                return self.left.get(key)


root = Node("M", 24)
root.insert("R", 22)
root.insert("I", 100)
root.insert("S", 24)
root.insert("V", 100)

root.get("R")
root.get("S")
root.get("V")
root.get("P")
