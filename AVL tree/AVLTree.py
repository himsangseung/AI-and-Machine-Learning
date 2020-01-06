'''
PROJECT 5 - AVL Trees
Name:Sang-Seung Jay Lee
'''

import random as r      # To use for testing

class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)

class AVLTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None    # The root Node of the tree
        self.size = 0       # The number of Nodes in the tree

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    def visual(self):
        """
        Returns a visual representation of the AVL Tree in terms of levels
        :return: None
        """
        root = self.root
        if not root:
            print("Empty tree.")
            return
        bfs_queue = []
        track = {}
        bfs_queue.append((root, 0, root.parent))
        h = self.height(self.root)
        for i in range(h+1):
            track[i] = []
        while bfs_queue:
            node = bfs_queue.pop(0)
            track[node[1]].append(node)
            if node[0].left:
                bfs_queue.append((node[0].left, node[1] + 1, node[0]))
            if node[0].right:
                bfs_queue.append((node[0].right, node[1] + 1, node[0]))
        for i in range(h+1):
            print(f"Level {i}: ", end='')
            for node in track[i]:
                print(tuple([node[0], node[2]]), end=' ')
            print()

    ### Implement/Modify the functions below ###

    def insert(self, node, value):
        '''
        Takes in a value to be added to the tree
        :param node: root node
        :param value: value of the node to be inserted
        :return: no return
        '''
        #if node is not None and node.value == value:
        #    return
        if self.root is None:
            # The root's parent is None.
            new_node = Node(value)
            self.root = new_node
            node = self.root
            self.size += 1

        elif node.value < value:
            if node.right is None:
                new_node = Node(value, node)
                node.right = new_node
                self.size += 1
            else:
                self.insert(node.right, value)
        elif node.value > value:
            if node.left is None:
                new_node = Node(value, node)
                node.left = new_node
                self.size += 1
            else:
                self.insert(node.left, value)

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        self.rebalance(node)

    def remove(self, node, value):
        """
        takes in a value to remove from the tree
        :param node: root node
        :param value: value of the node to be removed
        :return: no return
        """

        ###removal fucntion
        if self.root is None:
            # The root's parent is None.
            return None
        if node.value == value:
            if node is not None: # remove left pointers for all  if using max swap
                if (node.right is None and node.left is not None):
                    #do max and return thing
                    node.value = (self.max(node.left)).value #modifed 3/15 6:39pm
                    #(self.max(node.left)).parent = None
                    if (self.max(node.left)).parent.left.value == (self.max(node.left)).value:
                        (self.max(node.left)).parent.left = None
                    else:
                        (self.max(node.left)).parent.right = None

                    self.size -= 1

                elif node.right is not None and node.left is None:
                    node.value = node.right.value
                    node.left = node.right.left
                    node.right =node.right.right
                    self.size -=1

                elif node.right is not None and node.left is not None:

                    if node.left.left is None and node.left.right is None:
                        node.value = (self.max(node.left)).value
                        (self.max(node.left)).parent = node
                        (self.max(node.left)).parent.left = None

                    elif node.left.left is not None and node.left.right is None:
                        node.value = (self.max(node.left)).value
                        self.max(node.left).parent.left =  self.max(node.left).left

                    else:
                        node.value = (self.max(node.left)).value
                        self.max(node.left).parent.right = None


                    self.size -= 1


                else:
                    if node.value == self.root.value:
                        self.root = None
                        self.rebalance(node)
                        self.size -= 1
                        return None

                    if (node.parent.left is not None) and node.parent.left.value == node.value:
                        node.parent.left = None
                        self.size -= 1
                    else:
                        node.parent.right = None
                        self.size -= 1

        elif node.value < value:
            if node.right is None:
                return node
            else:

                self.remove(node.right, value)
        elif node.value > value:
            if node.left is None:
                return node
            else:

                self.remove(node.left, value)


        node.height = max(self.height(node.left), self.height(node.right)) + 1
        self.rebalance(node)




    def search(self, node, value):
        """
        Takes in a value to search for and return the found node
        :param node: root node
        :param value: value to be searched
        :return: if found, the node, if not, potential parent
        """

        if self.root is None:
            # The root's parent is None.

            return None
        if node.value == value:
            return node


        elif node.value < value:
            if node.right is None:
                return node
            else:
                return self.search(node.right, value)
        elif node.value > value:
            if node.left is None:
                return node
            else:
                return self.search(node.left, value)



    def inorder(self, node):
        """
        Traversing through inorder
        :param node: root node
        :return: generator object inorder method
        """
        if node is None:
            return

        yield from (self.inorder(node.left) )
        yield node
        yield from ( self.inorder(node.right) )

        #yield from new_list

    def preorder(self, node):
        """
        Traversing through preorder
        :param node: root node
        :return: generator object preorder method
        """
        if node is None:
            return
        yield node
        yield from self.preorder(node.left)
        yield from self.preorder(node.right)


    def postorder(self, node):
        """
        Traversing through postorder
        :param node: root node
        :return: generator object postorder method
        """
        if node is None:
            return
        yield from self.postorder(node.left)
        yield from self.postorder(node.right)
        yield node


    def depth(self, value):
        """
        the depth of the node with the given value
        :param value: value of the node to get depth of
        :return: depth of the node with the value
        """
        node = self.root
        cnt = 0
        while node is not None and node.value != value:

            if node.value < value:
                node = node.right
                cnt += 1
            else:
                node = node.left
                cnt += 1
        if node is None:
            return -1
        return cnt

    def height(self, node):
        """
        the height of the node with the given value
        :param node: root node
        :return: height of the at given node
        """
        if node is None:
            return -1
        else:
            return node.height



    def min(self, node):
        """
        finding minimum node value
        :param node: root node
        :return:return the minumum node value or default
        """

        if node is None:
            return None

        if node.left is None and node.right is None:
            return node
        if node.left is not None:
            return self.min(node.left)



    def max(self, node):
        """
        finding maximum node value
        :param node: root node
        :return: the maxmimum node value or default
        """
        if node is None:
            return None

        if node.left is None and node.right is None:
            return node
        if node.right is not None:
            return self.max(node.right)
        return node# added 3/19/2019 5:25pm



    def get_size(self):
        """
        size of the node
        :return: number of nodes
        """
        return self.root.size

    def get_balance(self, node):
        """
        getting balance factor for each node
        :param node: root node
        :return: balance factor of the node
        """
        left_height = -1
        right_height = -1

        if node.left is not None:
            left_height = node.left.height

        if node.right is not None:
            right_height = node.right.height
        return left_height - right_height


    def left_rotate(self, root):
        '''
        left rotation method around the root
        :param root: root node
        :return: the root node after rotation
        '''
        new_root = root.right
        new_root.parent = root.parent
        if new_root.parent is None:
            self.root = new_root
        else:
            if new_root.parent.right == root:
                new_root.parent.right = new_root
            else:
                new_root.parent.left = new_root
        root.right = new_root.left

        if root.right is not None:

            root.right.parent = root
        new_root.left = root
        root.parent = new_root

        #height update
        root.height = max(self.height(root.left), self.height(root.right)) + 1

        new_root.height = max(self.height(new_root.left), self.height(new_root.right)) + 1

        return self.root

    def right_rotate(self, root):
        '''
        right rotation method around the root
        :param root: root node
        :return: the root node after rotation
        '''
        new_root = root.left
        new_root.parent = root.parent
        if new_root.parent is None:
            self.root = new_root
        else:
            if new_root.parent.left == root:
                new_root.parent.left = new_root
            else:
                new_root.parent.right = new_root
        root.left = new_root.right

        if root.left is not None:
            root.left.parent = root
        new_root.right = root
        root.parent = new_root

        root.height = max(self.height(root.left), self.height(root.right)) + 1
        new_root.height = max(self.height(new_root.left), self.height(new_root.right)) + 1

        return self.root


    def rebalance(self, node):
        """
        manages rotation depending on balance factor
        :param node: root node
        :return: return root of the balanced subtree
        """

        if self.get_balance(node) == -2:# left right rotation
            if self.get_balance(node.right) == 1:
                self.right_rotate(node.right)
            return self.left_rotate(node)


        elif self.get_balance(node) == 2:
            if self.get_balance(node.left) == -1:
                self.left_rotate(node.left)
            return self.right_rotate(node)

        return node

def repair_tree(tree):
    """
    Takes in a tree with two values may have been swapped, swap back if needed
    :param tree: another tree root node
    :return: only repair the tree
    """
    lists = []
    lists_values = []
    lists2 = []

    result1 = tree.inorder(tree.root)
    for i in range(tree.size):
        new1 = next(result1, None)
        lists.append(new1)
        lists_values.append(new1.value)

    lists_values.sort()

    result1 = tree.inorder(tree.root)
    for i in range(tree.size):
        new1 = next(result1,None)

        print(new1)
        if new1.value != lists_values[i]:

            lists2.append(new1)
            continue
    if len(lists2) != 0:

        lists2[0].value , lists2[1].value = lists2[1].value, lists2[0].value
