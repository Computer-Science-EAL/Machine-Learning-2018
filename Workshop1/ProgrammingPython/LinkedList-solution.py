#!/bin/python

class LinkedList(object):
    # Inner class
    class Node(object):
        prev = None
        next = None

        def __init__(self, value):
            self.value = value

    # LinkedList fields
    first = None

    # LinkedList methods
    def add(self, value):
        if self.first is None:
            self.first = self.Node(value)
        else:
            tmp = self.first
            while tmp.next is not None:
                tmp = tmp.next
            node = self.Node(value)
            tmp.next = node
            node.prev = tmp


    def get(self, index):
        if self.first is None: return None
        tmp = self.first
        i = 0
        while i < index:
            tmp = tmp.next
            i += 1
            if tmp is None: return None
        return tmp.value


    def remove(self, index):
        if self.first is None: return None
        tmp = self.first
        i = 0
        while i < index:
            if tmp.next is None: return None
            tmp = tmp.next
            i += 1
        prev = tmp.prev
        next = tmp.next
        prev.next = next
        if next is not None: next.prev = prev
        return tmp.value


    def insert(self, value, index):
        if self.first is None: return None
        if index is 0: # if it's the first
            node = self.Node(value)
            node.next = self.first
            self.first.prev = node
            self.first = node
        else:
            tmp = self.first
            i = 0
            while i < index:
                tmp = tmp.next
                i += 1
                if tmp is None: return None
            node = self.Node(value)
            node.next = tmp
            node.prev = tmp.prev
            tmp.prev.next = node
            tmp.prev = node


    def __str__(self):
        output = "["
        tmp = self.first
        while tmp is not None:
            output += str(tmp.value) + ","
            tmp = tmp.next
        return output[:-1] + "]"



if __name__ == "__main__":
    ll = LinkedList()
    ll.add(4)
    ll.add(6)
    ll.add(6)
    ll.add(1)
    ll.add(3)
    print(ll)

    print(ll.get(3))
    print(ll.get(0))
    print(ll.get(5))

    print(ll.remove(2))
    print(ll.get(3))

    print(ll)

    ll.insert(11,1)
    ll.insert(80,4)
    ll.insert(50,0)

    print(ll)
