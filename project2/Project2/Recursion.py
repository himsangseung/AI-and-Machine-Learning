"""
PROJECT 2 - Recursion
Name:Sang-Seung Jay Lee
"""

class LinkedNode:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next_node'

    def __init__(self, value, next_node = None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)
    __str__ = __repr__


def insert(value, node=None):
    '''
    Inserts a value with node and returns head node
    :param value: Value to be inserted
    :param node: head of the node, with default None
    :return: returns the head node after insertion
    '''
    if node is None:
        new_node = LinkedNode(value)
        return new_node
    else:
        node.next_node = insert(value, node.next_node)
    return node

def string(node):
    '''
    returns string representation
    :param node: head Linklist node
    :return: returns string format of the node list
    '''

    if node.next_node is None:
        return "%s" %node.value
    else:
        return "%s, " %node.value + string(node.next_node)

def remove(value, node):
    '''
    removes the folliwng node with the value
    :param value: value to be removed
    :param node: head of the node list
    :return: returns the head of the node list after removal
    '''
    if node is None:
        return None
    if node.value == value:
        return node.next_node
    elif node.next_node is None:
        return node
    else:
        node.next_node = remove(value, node.next_node)
    return node


def remove_all(value, node):
    '''
    remove all instances of value and return head node
    :param value: value to be removed
    :param node: head node of the list
    :return: head of the node list after removals
    '''
    if node is None:
        return
    if node.value == value:
        return remove_all(value, node.next_node)
    elif node.next_node is None:
        return node
    elif node.value != value:
        node.next_node = remove_all(value, node.next_node)
    return node


def search(value, node):
    '''
    search through node with value and
    returns True for found if not False
    :param value: value to be searched
    :param node: head node of the list
    :return: boolean expression
    '''
    if node.value == value:
        return True
    elif node.next_node is None:
        return False
    else:
        if node.next_node is not None:
            return search(value, node.next_node)


def length(node):
    '''
    returns length of the node list
    :param node: head of the node list
    :return: integer value of the list
    '''

    if node is None:
        return 0
    elif node.next_node is None:
        return 1
    else:
        return 1 + length(node.next_node)


def sum_all(node):
    '''
    sum all instance values in the node list
    :param node: head of the node list
    :return: returns summed values in the node list
    '''
    if node is None:
        return 0
    if node is not None:
        return node.value + sum_all(node.next_node)


def count(value, node):
    '''
    counting how many times value appears in the node list
    :param value: value to be counted
    :param node: head node of the list
    :return: count in integer
    '''
    if node.value == value: #and node.next_node is not None:
        if node.next_node is not None:
            return 1 + count(value, node.next_node)
        else:
            return 1
    elif node.value != value and node.next_node is not None:
        return count(value, node.next_node)
    else:
        return 0

# Application Problem
def palindrome(node, length, compare):
    '''
    checking if the node list is a palindrome
    :param node: head node of the list to be checked
    :param length: length of the node list
    :param compare: a list with one element
    :return: boolean; if True it is palindrome elswise False
    '''
    if length == 1 or length == 0:
        return True
    if node is None:
        return
    if compare[0] is None:
        compare[0] = node
    palindrome(node.next_node, length, compare)

    if compare[0] is None:
        return False
    if node.value != compare[0].value:
        print("node", node, end=" ")
        print("compare", compare[0])
        compare[0] = node.next_node
        return False
    if compare[0].next_node is None:
        return True
    compare[0] = compare[0].next_node
