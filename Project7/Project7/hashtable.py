'''
PROJECT 7 - Hash Tables
Name: Sang-Seung Jay Lee
PID: A48858495
'''

class HashNode:
    """
    DO NOT EDIT
    """
    __slots__ = ["key", "value", "deleted"]

    def __init__(self, key, value, deleted=False):
        self.key = key
        self.value = value
        self.deleted = deleted

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


class HashTable:
    """
    Hash Table Class
    """
    __slots__ = ['capacity', 'size', 'table', 'collisions', 'prime_index']

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity=8):
        """
        DO NOT EDIT
        Initializes hash table
        :param capacity: capacity of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        i = 0
        while HashTable.primes[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
        DO NOT EDIT
        Represents the table as a string
        :return: string representation of the hash table
        """
        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    def __setitem__(self, key, value):
        """
        DO NOT EDIT
        Allows for the use of the set operator to insert into table
        :param key: string key to insert
        :param value: value to insert
        :return: None
        """
        return self.insert(key=key, value=value)

    def __getitem__(self, item):
        """
        DO NOT EDIT
        Allows get operator to retrieve a value from the table
        :param item: string key of item to retrieve from tabkle
        :return: HashNode
        """
        return self.get(item)

    def __contains__(self, item):
        """
        DO NOT EDIT
        Checks whether a given key exists in the table
        :param item: string key of item to retrieve
        :return: Bool
        """
        if self.get(item) is not None:
            return True
        return False

    def _hash_1(self, key):
        """
        ---DO NOT EDIT---
        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def _hash_2(self, key):
        """
        ---DO NOT EDIT---
        Converts a string x into a hash
        :param x: key to be hashed
        :return: a hashed value
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        prime = HashTable.primes[self.prime_index]

        hashed_value = prime - (hashed_value % prime)
        if hashed_value % 2 == 0:
            hashed_value += 1
        return hashed_value


    """ **************** Student Section Below ******************************"""
    def hash(self, key, inserting=False):
        '''
        Given a key string return a index in the hash table
        :param key: key string
        :param inserting: Differeinatiting parameter for hasing for an index
        :return: next avialble empty position in the table or the index
        '''
        index = self._hash_1(key)
        if inserting == False:#deletin or lookup,
            if self.get(key) is not None: # already exists,
                while self.table[index].key != key:
                    index = (index + self._hash_2(key))% self.capacity
                return index
            else:
                while self.table[index] is not None:
                        index = (index + self._hash_2(key)) % self.capacity
                return index

        else:# insertion
            if self.get(key) is not None:# Hashnode with key already exists, update.
                while self.table[index].key != key:
                    index = (index + self._hash_2(key)) % self.capacity
                return index
            else:

                while self.table[index] is not None:
                    if self.table[index].deleted:# if on deleted node, return index
                        return index
                    else:# if not, go to next index with _hash_2
                        index = (index + self._hash_2(key)) % self.capacity
                return index

    def insert(self, key, value):
        '''
        inserts the hashnode with key and value to the next bin
        :param key: key of interest
        :param value: value of interest
        :return: None
        '''
        new_node = HashNode(key, value)
        insert_idx = self.hash(key, True)
        new_node.key = key
        new_node.value = value
        self.size += 1
        self.table[insert_idx] = new_node
        load_factor = self.size / self.capacity

        if load_factor >= 0.5:
            self.grow()

        # if load factor 0.5 or larger grow() after inserting in
        return None


    def get(self, key):
        '''
        obtains hashnode where the key is in
        :param key: key of interest
        :return: None
        '''
        for i in self.table:
            if i is None:
                continue
            elif i.key == key:
                return i
        return None


    def delete(self, key):
        '''
        takes in a key of interest and remove the hashnode
        :param key: key of intersete
        :return: None
        '''
        index = self.hash(key)
        if self.table[index].key == key:
            self.table[index].key = None
            self.table[index].value = None
            self.table[index].deleted = True
            self.size -= 1

    def grow(self):
        '''
        grows the capacity to twice as its value
         when loading factor meets 0.5
        :return: None
        '''
        self.capacity *= 2
        new_list = [None]*self.capacity
        ori_list = self.table
        self.table = new_list
        i = 0
        while HashTable.primes[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1
        # rehasehs each value to the new list
        for j in range(self.capacity//2):
            if ori_list[j] is not None and ori_list[j].deleted == False:
                new_index = self.hash(ori_list[j].key)
                self.table[new_index] = ori_list[j]

def word_frequency(string, lexicon, table):
    '''
    the method puts in sub strings into table and lays out the information on hash table
    with frequency inforamtion
    :param string: concatenated strings
    :param lexicon: lists or dictionary keys of sub-stgrings in string
    :param table: hashtable to be used
    :return:
    '''

    lists =[]
    for k in lexicon:
        lists.append(k)
    lexicon = lists

    for j in range(len(lexicon)):
        table.insert(lexicon[j], 0)
    i = 0

    while string != "":
        if i >= len(string):
            break

        if string[i:] in lexicon:
            j = 0
            if string == string[i:]:
                table[string[i:]].value += 1
                break
            while string[j:-len(string[i:])] != "":
                #print(string[i:])
                #print(string[j:-i])
                if string [j:-len(string[i:])] in lexicon:
                    table[string[i:]].value += 1
                    string = string [:-len(string[i:])]
                    i = -1
                    break
                j += 1
        i += 1

    return table



