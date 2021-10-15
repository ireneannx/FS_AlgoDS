LinkedList = __import__('w3_linkedlist').LinkedList
Node = __import__('w3_linkedlist').Node


class DoubleNode(Node):

    def __init__(self, data):
        self._data = data
        self._next = None
        self._before = None

    @property
    def before(self):
        return self._before

    @before.setter
    def before(self, new_before):
        if isinstance(new_before, Node) or new_before is None:
            self._before = new_before
        else:
            raise TypeError
