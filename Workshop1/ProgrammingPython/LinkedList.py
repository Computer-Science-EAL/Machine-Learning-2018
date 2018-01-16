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
        pass

    def get(self, index):
        pass

    def remove(self, index):
        pass

    def insert(self, value, index):
        pass

    def __str__(self):
        return ""


if __name__ == "__main__":
    ll = LinkedList()
    print(ll)
