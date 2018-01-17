#! /usr/bin/python

'''
Created by: Silverbaq @ 2018
'''

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

    def remove(self, value):
        if self.first is None: return None
        tmp = self.first
        while tmp is not None:
            if tmp.value is value:
                next = tmp.next
                prev = tmp.prev
                if prev is not None: prev.next = next
                if next is not None: next.prev = prev
                return tmp.value
            tmp = tmp.next
        return None


    def remove_at(self, index):
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
        if index is 0:  # if it's the first
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

    def contains(self, value):
        if self.first is None: return False
        tmp = self.first
        while tmp is not None:
            if tmp.value is value: return True
            tmp = tmp.next
        return False

    def size(self):
        tmp = self.first
        count = 0
        while tmp is not None:
            count += 1
            tmp = tmp.next
        return count

    def clear(self):
        self.first = None

    def __str__(self):
        if self.first is None: return "[]"
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
    print('The linked list looks like this:\t\t {}'.format(ll))
    print('')
    print('Finding the value at index 3:\t\t\t {}'.format(ll.get(3)))
    print('Finding the value at index 0:\t\t\t {}'.format(ll.get(0)))
    print('Finding the value at index 5:\t\t\t {}'.format(ll.get(5)))
    print('')
    print('Removing the value at index 2:\t\t\t {}'.format(ll.remove_at(2)))
    print('Finding the value at index 3:\t\t\t {}'.format(ll.get(3)))
    print('')
    print('Inserting the value 4 at index 2:\t\t {}'.format(ll.insert(4,2)))
    print('')
    print('The linked list looks like this:\t\t {}'.format(ll))
    print('Removing the value 1: \t\t\t\t'.format(ll.remove(1)))
    print('')
    print('The linked list looks like this:\t\t {}'.format(ll))
    print('')
    print('Inserting the value 11 at index 1:\t\t {}'.format(ll.insert(11, 1)))
    print('Inserting the value 80 at index 4:\t\t {}'.format(ll.insert(80, 4)))
    print('Inserting the value 50 at index 0:\t\t {}'.format(ll.insert(50, 0)))
    print('')
    print('')
    print('The list current size is:\t\t\t\t {}'.format(ll.size()))
    print('Does the list contain the value 11:\t\t {}'.format(ll.contains(11)))
    print('Does the list contain the value 123:\t {}'.format(ll.contains(123)))
    print('The linked list looks like this:\t\t {}'.format(ll))
    print('')
    print('Clearning the linked list:\t\t\t\t {}'.format(ll.clear()))
    print('The list current size is:\t\t\t\t {}'.format(ll.size()))
    print('The linked list looks like this:\t\t {}'.format(ll))