class Node():
    """
    This class represents the Node of the LinkedList.
    The instance variables are public for simplicity.
    There is no need for getters or setters.

    The instances variables of this class include:
    1. self.data: holds the data for the Node.
    2. self.next: holds the pointer to the next Node.

    The class methods include:
    a. __init__: This method is the constructor and it initializes
                 each instance variable.
    b. __str__: This method returns the data instance variable as
                a string.
    """

    def __init__(self, item):
        """
        Constructor:
        Sets the data instance variable to the item parameter
        Sets the next instance variable to None
        """
        self.data = item
        self.next = None

    def __str__(self):
        """
        Returns the data instance variable as a string
        """
        return str(self.data)



class LinkedList:
    """
    This class is an implementation of the Singly LinkedList ADT
    where both a head pointer and a tail pointer are used. The
    number of Nodes in the list is kept and updated as Nodes are
    added and removed. It uses protected instance variables, so
    that the child classes can get direct access.

    The instances variables of this class include:
    1. self._head: holds a pointer to the first Node.
    2. self._tail: holds a pointer to the last Node.
    3. self._size: hold the number of Nodes on the LinkedList

    The class methods include:
    a. __init__: This method is the constructor. It initializes
                 the protected instance variables.
    b. __len__: This method returns the number of Nodes in the
                 LinkedList.
    c. is_empty: This method returns True, if the LinkedList is
                 empty and False, otherwise.
    d. add_first: This method creates a new Node with the passed
                  in item and adds the Node as the first Node of
                  the LinkedList.
    e. add_last: This method creates a new Node with the passed
                 in item and adds the Node as the last Node of
                 the LinkedList.
    f. remove_first: This method removes the first Node of the
                     LinkedList and returns it
    g. __str__(self): This method returns the data of the
                      LinkedList as a string
    """

    def __init__(self):
        """
        Constructor:
        Uses protected instance variables
        Sets the head instance variable to None
        Sets the tail instance variable to None
        Sets
        the linked list size to 0
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """
        Returns the number of Nodes in the LinkedList.
        """
        return self._size

    def is_empty(self):
        """
        Returns True, if LinkedList is empty.
        Returns False, otherwise.
        """
        return len(self) == 0

    def add_first(self, item):
        """
        Creates a new Node with the given item.
        Adds the Node as the first element of the LinkedList.
        Updates both the head and tail pointers.
        Increments the number of Nodes in the LinkedList.
        """
        new_node = Node(item)
        new_node.next = self._head
        self._head = new_node

        if self.is_empty():
            self._tail = new_node
        self._size += 1

    def add_last(self, item):
        """
        Creates a new Node with the given item.
        Adds the Node as the last element of the LinkedList.
        Call add_first, if thre list is empty.
        Updates both the head and tail pointers.
        Increments the number of Nodes in the LinkedList.
        """
        if self.is_empty():
            self.add_first(item)
        else:
            new_node = Node(item)
            self._tail.next = new_node
            self._tail = new_node
            self._size += 1

    def remove_first(self):
        """
        Removes the 1st Node of the LinkedList and returns its data.
        Returns None, if LinkedList is empty.
        Updates both the head and tail pointers.
        Decrements the number of Nodes in the LinkedList.
        """
        if self.is_empty():
            return None
        current = self._head
        self._head = current.next
        self._size -= 1

        if self.is_empty():
            self._tail = None

        return current.data

    def __str__(self):
        """
        Return the contents of the LinkedList as a string
        with each Node's data on a separate line starting
        with the head of the LinkedList.
        """
        data_str = ""
        current = self._head
        for d in range(len(self)):
            data_str += str(current.data) + '\n'
            current = current.next
        return data_str


