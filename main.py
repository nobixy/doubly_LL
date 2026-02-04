"""Doubly Linked List implementation.

A linear data structure where each node contains a reference to both
the previous and next nodes, allowing bidirectional traversal.
"""

class Node:
    """Represents a single node in the doubly linked list.

    Attributes:
        value: The data stored in the node.
        prev: Reference to the previous node.
        next: Reference to the next node.
    """

    def __init__(self, value):
        """Initializes a new node with the given value.

        Args:
            value: The data to store in the node.
        """

class DoublyLinkedList:
    """Doubly linked list data structure.

    Attributes:
        head: Reference to the first node.
        tail: Reference to the last node.
        length: Number of nodes in the list.
    """

    def __init__(self, value):
        """Initializes the list with a single node.

        Args:
            value: The data for the initial node.
        """
        pass

    # MVP Methods

    def append(self, value):
        """Adds a new node to the end of the list.

        Args:
            value: The data for the new node.

        Returns:
            The updated list.
        """
        pass

    def prepend(self, value):
        """Adds a new node to the beginning of the list.

        Args:
            value: The data for the new node.

        Returns:
            The updated list.
        """
        pass

    def insert(self, index, value):
        """Inserts a new node at the specified index.

        Args:
            index: The position to insert at.
            value: The data for the new node.

        Returns:
            The updated list.
        """
        pass

    def pop(self):
        """Removes and returns the last node in the list.

        Returns:
            The removed node.
        """
        pass

    def delete(self, index):
        """Removes the node at the specified index.

        Args:
            index: The position of the node to remove.

        Returns:
            The removed node.
        """
        pass

    def search(self, value):
        """Finds the index of the first node containing the value.

        Args:
            value: The data to search for.

        Returns:
            The index of the node, or -1 if not found.
        """
        pass
