# Single Linked List
'''
class SLL:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new):
        self.next = new


node1 = SLL(10)
node2 = SLL(20)
node3 = SLL(30)

node1.set_next(node2)
node2.set_next(node3)


def display():
    out = []
    ptr = node1
    while ptr != None:
        out += [ptr.get_data()]
        ptr = ptr.get_next()
    print(out)


display()
'''

































































