'''
PROJECT 6 - Heaps
Name: Sang-Seung Jay Lee
PID: A48858495
'''

class Node:
    """
    Class definition shouldn't be modified in anyway
    """
    __slots__ = ('_key', '_val')

    def __init__(self, key, val):
        self._key = key
        self._val = val

    def __lt__(self, other):
        return self._key < other._key or (self._key == other._key and self._val < other._val)

    def __gt__(self, other):
        return self._key > other._key or (self._key == other._key and self._val > other._val)

    def __eq__(self, other):
        return self._key == other._key and self._val == other._val

    def __str__(self):
        return '(k: {0} v: {1})'.format(self._key, self._val)

    __repr__ = __str__

    @property
    def val(self):
        """
        :return: underlying value of node
        """
        return self._val


class Heap:
    """
    Class definition is partially completed.
    Method signatures and provided methods may not be edited in any way.
    """
    __slots__ = ('_size', '_capacity', '_data')

    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity + 1  # additional element space for push
        self._data = [None for _ in range(self._capacity)]

    def __str__(self):
        return ', '.join(str(el) for el in self._data if el is not None)

    __repr__ = __str__

    def __len__(self):  # allows for use of len(my_heap_object)
        return self._size

#    DO NOT MODIFY ANYTHING ABOVE THIS LINE
#    Start of Student Modifications

    def _percolate_up(self):
        '''
        When the element exists in the last spot, move up and swap if the condition meets
        :return: returns None
        '''
        last_node = self._data[self._size-1]
        index = self._size -1
        while index != 0:

            if self._data[index] < self._data[(index -1) //2]:
                self._data[index], self._data[(index -1) //2] \
                    = self._data[(index -1) //2], self._data[index]
            index = (index -1) //2
        return None


    def _percolate_down(self):
        '''
        when the element exists in the first spot, move down and swap if the condition meets
        :return: return NonE
        '''
        first_node = self._data[0]
        index = 0
        if (index == 0 and self._size == 1) or self._size == 0:
            return None
        while index == 0 or not (index == self._size or index == self._size -1) and index != -1:

            min_child_index = self._min_child(index)
            if min_child_index != -1 and self._data[min_child_index] < self._data[index]:
                self._data[index], self._data[min_child_index] \
                    = self._data[min_child_index], self._data[index]
            index = min_child_index
        return None


    def _min_child(self, i):
        '''
        with given index, get the smallest child of the node
        :param i: index of node
        :return: index of minimum child as an integer
        '''
        if 2*i +1 > self._size -1:
            return -1 #leaft node
        #elif 2*i +2 == self._size -1: #take out  3/26 10:16am
        #    return 2*i+2
        elif 2*i+1 == self._size -1:
            return 2*i+1
        else:
            if self._data[2*i + 1] > self._data[2*i + 2]:
                return 2*i+2
            return 2*i+1


    def push(self, key, val):
        '''
        takes in key and val, makes a node and added to the heap
        pops when the size meets capacity
        :param key: key of the node
        :param val: value of the node
        :return: returns None
        '''
        new_node = Node(key, val)
        self._data[self._size] = new_node
        self._size += 1

        self._percolate_up()
        if self._capacity <= self._size:

            self.pop()
        return None


    def pop(self):
        '''
        removes the smallest element(at first index) from the heap
        :return: value of the node
        '''
        if self.empty:
            return None
        smallest_ele = self._data[0]
        self._data[0] = None
        self._data[self._size-1], self._data[0] = self._data[0], self._data[self._size-1]
        self._size -= 1

        self._percolate_down()
        return smallest_ele.val

    @property  # do not remove
    def empty(self):
        '''
        chekcing if the heap is empty
        :return: Boolean, True if empty, otherwise False
        '''
        if self._size:
            return False
        return True


    @property  # do not remove
    def top(self):
        '''
        gives the root value
        :return:  root value
        '''
        if self.empty == False:
            return self._data[0].val
        return None

    @property  # do not remove
    def levels(self):
        '''
        get the list of lists of node values at a single level
        :return: lists of node.val lists
        '''
        new_lists = []
        i = 0
        new_list = []
        for j in range(self._size):
            new_list = self._data[i:2*i+1]
            if new_list != []:# or all None:
                new_lists.append(new_list)

            i = 2*i+1
        if new_lists != []:
            for k in range(len(new_lists[-1])):
                print(new_lists[-1][k])
                if new_lists[-1][k] is None:
                    del new_lists[-1][k:]
                    break
        if new_lists[-1] == []:
            new_lists.pop()

        return new_lists


def most_x_common(vals, X):
    '''
    getting the X most commonly occuring elements in set
    :param vals: list of interest
    :param X: number of elements to be returned
    :return: a set of values of node that most occuring at given X number
    '''
    dicts = {}
    for val in vals:

        if val in dicts.keys():
            dicts[val] += 1
        else:
            dicts[val] = 1
    print(dicts)

    new_heap = Heap(X)
    for k, v in dicts.items():
        new_heap.push(v, k)
    new_set = set()
    for i in range(X):
        new_set.add(new_heap._data[i].val)
    return new_set
