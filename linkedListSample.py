class Node:
    def __init__(self) :
        self.data = None
        self.next = None


class LinkedLists:
    def __init__(self):
        self.previous = None
    def add(self,data):
        node = Node()
        node.data = data
        node.next = self.previous
        self.previous = node
        print "added node as %s and next as %s" %(node.data, node.next)

    def print_list(self):
        node = self.previous
        while node:
            print node.data
            node = node.next


class blaa(LinkedLists):



linked_list = LinkedLists()
linked_list.add(2)
linked_list.add(4)
linked_list.add(6)

linked_list.print_list()
