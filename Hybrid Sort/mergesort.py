"""
PROJECT 3 - Merge Sort
Name: SangSeung Lee
"""

from Project3.LinkedList import LinkedList

def merge_lists(lists, threshold):
    '''
    :param lists: lists of singly linked list
    :param threshold: threshold for using insertion sort of merge sort
    :return: one combined linked list
    '''
    new_list = LinkedList()
    if len(lists) == 1:
        list = lists[0]
        list = merge_sort(list, threshold)
        new_list = merge(new_list, list)
        return new_list

    if lists is None:
        return

    for list in lists:
        list = merge_sort(list, threshold)
        new_list = merge(new_list, list)
    return new_list

def merge_sort(linked_list, threshold):
    '''
    :param linked_list: list to be sorted
    :param threshold: if larger than length merge sort, else insertion sort
    :return: sorted list
    '''

    n = linked_list.length()
    if n < 2:
        return linked_list
    elif n > threshold:
        f1, f2 = split_linked_list(linked_list)
        f1 = merge_sort(f1, threshold)
        f2 = merge_sort(f2, threshold)
        return merge(f1, f2)

    else:
        linked_list.insertion_sort()
        return linked_list

def split_linked_list(linked_list):
    '''
    :param linked_list: list to be split in half
    :return: tuples of two divided linked lists
    '''
    cnt_index = linked_list.length()//2
    cnt = 1
    front_link = LinkedList()
    back_link = LinkedList()

    while not linked_list.is_empty():
        if cnt <= cnt_index:
            front_link.push_back(linked_list.pop_front())
            cnt = cnt+1
        else:
            back_link.push_back(linked_list.pop_front())

    return (front_link, back_link)


def merge(list1, list2):
    '''
    :param list1: first list to be combined
    :param list2: second list to be combined
    :return: one complete combined list
    '''
    new_linked = LinkedList()

    while list1.front_value() is not None or list2.front_value() is not None:
        if list1.is_empty():
            new_linked.push_back(list2.pop_front())

        elif list2.is_empty():
            new_linked.push_back(list1.pop_front())
        elif list1.front_value() > list2.front_value():
            new_linked.push_back(list2.pop_front())

        else:
            new_linked.push_back(list1.pop_front())

    return new_linked
'''
    link = LinkedList()
    link.push_back(7)
    link.push_back(1)
    link.push_back(4)
    link.push_back(2)
    
    link2 = LinkedList()
    link2.push_back(33)
    link2.push_back(11)
    link2.push_back(42)
    link2.push_back(24)
    
    link3 = LinkedList()
    link3.push_back(75)
    link3.push_back(13)
    link3.push_back(42)
    link3.push_back(26)
    
    #(merge_sort(link, 0))
    list = []
    list.append(link)
    list.append(link2)
    list.append(link3)
    print( merge_lists(list, 10))
    #print(link)
    
    
    link = LinkedList()
    link.push_back(7)
    link.push_back(1)
    link.push_back(4)
    link.push_back(2)
    link.insertion_sort()
    print(link)
    
    
    
    ##large number test
    
    orig = [randint(-1000000,100000000000) * choice([-1,1]) for _ in range(50)]
    orig2 =[randint(-1000000,100000000000) * choice([-1,1]) for _ in range(50)]
    orig3 =[randint(-1000000,100000000000) * choice([-1,1]) for _ in range(50)]
    
    list = []
    llist = LinkedList(orig)
    llist2 = LinkedList(orig2)
    llist3 = LinkedList(orig3)
    
    list.append(llist)
    list.append(llist2)
    list.append(llist3)
    
    list = merge_lists(list,2e20)
    list2 = orig + orig2 + orig3
    
    print(list)
    
    print(list.length())
    
    list2 = sorted(list2)
    print(list2)
    print(len(list2))
    
    
    ######################
    list = []
    list2 =[]
    for i in range(-100,100):
        list.append(i)
    list.append(list)
    linked = LinkedList(list)
    print(linked)
    list2.append(linked)
    print(list2)
    output = merge_lists(list2,300)
    print(output)    

    a = LinkedList([1,-2000])
    list =[]
    list.append(a)
    #print(list)
    print( merge_lists(list,20) )
'''
