#!/usr/bin/python3
"""Defining a node class of a singly linked list called Node."""


class Node:
    """Node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes new instance of Node class.

        Args:
            data (int) The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the current data in the node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets the data of the node."""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Gets te next_node of the current node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node of te current node."""
        if not (value is None or isinstance(value, Node)):
            raise TypeError('next)node must be a node object')
        self.__next_node = value


"""Defining a singly linked list class called SinlyLinkedList."""


class SinglyLinkedList:
    """A singly linked list inheriting the Node class."""

    def __init__(self):
        """Initializing the singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts value into the list in a sorted manner.

        inserts a new Node into the correct sorted positione
            in the list (increasing order).

        Args:
            value (int): The value of the new node to be inserted
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
            return
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """prints each node of the SinglyLinkedList"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
