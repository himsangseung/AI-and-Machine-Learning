########################################
# PROJECT 1 - Linked List
# Author:  SangSeung (Jay) lee
# PID: A48858495
########################################

class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next_node'

    def __init__(self, value, next_node=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node

    def __eq__(self, other):
        """
        DO NOT EDIT
        Determine if two nodes are equal (same value)
        :param other: node to compare to
        :return: True if nodes are equal, False otherwise
        """
        if other is None:
            return False
        if self.value == other.value:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)

    __str__ = __repr__


class LinkedList:
    def __init__(self):
        """
        DO NOT EDIT
        Create/initialize an empty linked list
        """
        self.head = None   # Node
        self.tail = None   # Node
        self.size = 0      # Integer

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """

        if self.size != other.size:
            return False
        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next_node
                temp_other = temp_other.next_node
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a linked list
        :return: string of list of values
        """
        temp_node = self.head
        values = []
        if temp_node is None:
            return None
        while temp_node is not None:
            values.append(temp_node.value)
            temp_node = temp_node.next_node
        return str(values)

    __str__ = __repr__

    ###### students modify the below functions #####

    # ------------------------Accessor Functions---------------------------

    def length(self):
        """
        the number of nodes in the list
        :return: the number of nodes in the list
        """
        return self.size

    def is_empty(self):
        """
        checks the content existence of the list
        :return: if the node is empty returns True, else, False
        """
        return True if self.size == 0 else False

    def front_value(self):
        """
        value of the head node
        :return: the value of the head node,
                but if the list is empty, returns None
        """
        if self.size == 0:
            return None
        else:
            return self.head.value

    def back_value(self):
        """
        tail node value of the linkedlist
        :return: tail value of the linkedlist
                 if the list is empty, returns None
        """
        if self.size == 0:
            return None
        else:
            return self.tail.value

    def count(self, val):
        """
        checks number of input value(val)'s appearance in the list
        :param val: value which will be checked for count
        :return: how many times val occurs in the list
        """
        cnt = 0
        node_head = self.head
        while node_head is not None:
            if node_head.value == val:
                cnt += 1
            node_head = node_head.next_node

        return cnt

    def find(self, val):
        """
        finds the value in the list
        :param val: value to be found
        :return: if found True, else (Default)False
        """
        node_head = self.head
        while node_head is not None:
            if node_head.value == val:
                return True
            node_head = node_head.next_node
    #------------------------Mutator Functions---------------------------

    def push_front(self, val):
        """
        adds a value on the list on the front
        :param val: value to be added
        :return: returns default(not set to return anything)
        """
        new_node = Node(val, self.head)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.size += 1

    def push_back(self, val):
        """
        adds a value on the list on the back
        :param val: value to be added
        :return: returns default(not set to return anything)
        """
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if self.size == 1:
                self.head.next_node = new_node
                self.tail = new_node
            else:
                self.tail.next_node = new_node
                self.tail = new_node
        self.size += 1

    def pop_front(self):
        """
        pops out a value from the front
        :return: popped value or if list is empty, return None
        """
        if self.size == 0:
            return None
        elif self.size == 1:
            head_node = self.head
            self.head = None
            self.tail = None
            self.size -= 1 #added
            return head_node.value
        else:
            previous_node = self.head
            self.head = self.head.next_node
            self.size -= 1
            return previous_node.value

    def pop_back(self):
        """
        pops out a value from the back
        :return: popped value or if list is empty, return None
        """
        end_node = self.tail
        head_node = self.head
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1#added
            return head_node.value

        while head_node is not None:
            if head_node.next_node == end_node:
                head_node.next_node = None
                self.tail = head_node
            head_node = head_node.next_node
        self.size -= 1

        return end_node.value

def partition(linked_list, x):
    """
    partitions the original list
    :param linked_list: original list
    :param x: partition standard value
    :return: partitioned list
    """
    new_list_less = LinkedList()
    new_list_other = LinkedList()
    pop_value = linked_list.pop_front()
    while pop_value is not None:
        if pop_value < x:
            new_list_less.push_back(pop_value)
        else:
            new_list_other.push_back(pop_value)

        pop_value = linked_list.pop_front()

    pop_value2 = new_list_other.pop_front()
    while pop_value2 is not None:
        new_list_less.push_back(pop_value2)
        pop_value2 = new_list_other.pop_front()

    new_list = new_list_less
    return new_list


llist = LinkedList()
llist.push_back(5)
llist.push_back(4)
llist.push_back(2)
llist.push_back(1)
llist.push_back(7)
llist.push_back(6)
llist.push_back(5)

llist = partition(llist, 3)
#assert str(llist) == "[2, 1, 5, 4]"
print(llist)

llist2 = LinkedList()
llist2.push_back(5)
llist2.push_back(4)
llist2.push_back(2)
llist2.push_back(1)

llist2 = partition(llist2, 7)
#assert str(llist2) == "[5, 4, 2, 1]"
print(llist2)

llist3 = LinkedList()
llist3.push_back(5)
llist3.push_back(4)
llist3.push_back(2)
llist3.push_back(1)

llist3 = partition(llist3, 2)
print(llist3)