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
        # TODO: implement this method
        pass

    def get(self, index):
        # TODO: implement this method
        pass

    def remove(self, index):
        # TODO: implement this method
        pass

    def insert(self, value, index):
        # TODO: implement this method
        pass

    def __str__(self):
        return ""


if __name__ == "__main__":
    ll = LinkedList()
    print(ll)
    # TODO: write "tests" as you implement different methods in your data structure
