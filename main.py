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
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """Doubly linked list data structure.

    Attributes:
        head: Reference to the first node.
        tail: Reference to the last node.
        length: Number of nodes in the list.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, value):
        """Adds a new node to the end of the list.

        Args:
            value: The data for the new node.

        Returns:
            The updated list.
        """
        node = Node(value)
        if self.head is None:
          self.head = node
          self.tail = node
          self.head.next = None
          self.tail.next = None
        else:
          old_tail = self.tail
          self.tail = node
          self.tail.next = None
          old_tail.next = self.tail

    def prepend(self, value):
        """Adds a new node to the beginning of the list.

        Args:
            value: The data for the new node.

        Returns:
            The updated list.
        """
        node = Node(value)
        if self.head is None:
          self.head = node
          self.tail = node
        else:
          old_head = self.head
          self.head = node
          self.head.next = old_head

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

    def __str__(self):
      if self.head is None:
        return "Empty"

      res = "LinkedList: "
      curr = self.head
      while curr is not None: # The end of the linked is is a null pointer to None
        res += str(curr.value)
        if curr.next is not None:
          res += " <---> "
        elif curr.next is None:
          res += " ---> None "
        curr = curr.next
      return res

ll = DoublyLinkedList()
ll.prepend(101)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.prepend(100)
print(ll)
