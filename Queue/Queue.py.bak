"""
PROJECT 4 - QUEUES
Name: Sang-Seung Jay Lee
PID: A48858495
"""


class CircularQueue:
    """
    Circular Queue Class
    """
    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        DO NOT MODIFY.
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0


    def __eq__(self, other):
        """
        DO NOT MODIFY.
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    def __str__(self):
        """
        DO NOT MODIFY.
        String representation of the queue
        :return: the queue as a string
        """
        if self.is_empty():
            return "Empty queue"
        result = ""
        str_list = [str(self.data[(self.head + i)%self.capacity]) for i in range(self.size)]
        return "Queue: " + (", ").join(str_list)

    # -----------MODIFY BELOW--------------
    def __len__(self):
        '''

        :return: len() returns length of the queue(size)
        '''
        return self.size

    def is_empty(self):
        '''

        :return: is_empty returns true if queue is empty and false if not
        '''
        return self.size == 0

    def head_element(self):
        '''

        :return:head elements gives the first element of the queue
        '''
        if self.head is not None:
            #a = self.data
            #b = self.head
            #c = self.tail
            return self.data[self.head]

    def tail_element(self):
        '''

        :return: tail_element gives last element of the queue
        '''
        if self.tail is not None:
            return self.data[self.tail-1]

    def enqueue(self, val):
        '''
        enqueue adds the value(val) to the end (or top) of the queue
        if the capacity is reached,
        it calls grow function and, head and tail are modified accordingly.
        :param val: the value to be added to the queue
        :return: returns None
        '''

        if self.tail >= self.capacity:# NEW CASE....
            self.tail = self.tail%self.capacity
        if self.head >= self.capacity:
            self.head = self.head%self.capacity
        self.data[self.tail] = val
        self.size += 1
        self.tail += 1
        if self.size == self.capacity:
            self.grow()

        return None

    def dequeue(self):
        '''
        dequeue functions as pop_front, pops out the first element of the queue
        if the capacity is reached(1/4 of original)
        it calls shrink and, head and tail are modified accordingly.
        :return: returns the element that is popped out of the queue
        '''
        new = self.data[self.head]
        if self.size == 0:
            return
        self.data[self.head] = None
        self.size -= 1
        self.head += 1
        if self.size <= self.capacity * 1 / 4 and self.capacity >= 8:
            self.shrink()
            self.tail = self.size
        return new





    def tail_dequeue(self):
        '''
        tail_dequeue works as an pop. if the capacity is reached(1/4 of original)
        it calls shrink and, head and tail are modified accordingly.
        :return: returns the popped element
        '''

        new = self.data[self.tail-1]

        if self.size == 0:
            return

        if self.size <= self.capacity * 1/4 + 1 and self.capacity >= 8:
            self.shrink()
            self.tail = self.capacity // 2

            self.data[self.tail] = None
            self.size -= 1


        else:
            self.data[self.tail-1] = None
            self.size -= 1
            #print("deque dataL",self.data)
            #print("deque size: ",self.size)
            #self.head += 1
            self.tail -= 1


        return new




    def grow(self):
        '''
        when the size of the queue reaches the capacity, it doubles the capacity
        :return: no return but capcity of the queue is modified
        '''
        lists = self.data
        self.capacity *= 2
        self.data = [None]*self.capacity
        cnt = 0

        while self.head != self.tail:

        #2.25.2015 edit for lists [none, noe, 3, 4 ...] make it head [3, 4 ...]

            self.data[self.head] = lists[cnt]
            self.head += 1
            cnt += 1
        self.head = 0


    def shrink(self):
        '''
        when the size of the queue reaches the capacity limit, it halves the capacity
        :return: no return but capcity of the queue is modified
        '''
        lists = self.data
        self.capacity //= 2
        self.data = [None]*self.capacity
        #cnt = 0

        self.head = 0
        for i in lists:
            if i is not None:
                self.data[self.head] = i
                self.head += 1

        self.head = 0


def greatest_val(w, values):
    '''
    finds the greatest value of size w and goes on to next starting element
    and stores the max value of each run to the new list
    :param w: length or size to be used
    :param values: list of values to be used
    :return: returns the list of greatest values of size w runs
    '''
    new_list = []
    _max = 0
    new_queue = CircularQueue()
    for i in range(len(values)-w+1):
        for j in range(w):
            if j == 0:
                a = (values[i+j])
                new_queue.enqueue(values[i+j])
                continue
            else:

                if new_queue.head_element() > values[i+j]:
                    continue
                else:
                    new_queue.dequeue()
                    new_queue.enqueue(values[i+j])

        new_list.append(new_queue.dequeue())
    if w == 0:
        return []
    return new_list
