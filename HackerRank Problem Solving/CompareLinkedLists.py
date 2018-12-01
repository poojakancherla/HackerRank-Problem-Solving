import LinkedListBase as l

# Function to compare the two linked lists
def compare_lists(llist1, llist2):

    l1 = l.length(llist1)
    l2 = l.length(llist2)

 # if the linked lists are of different lengths, directly return 0
    if l1 != l2:
        return 0

 # compare the heads of both lists
 # if equal, point to the next nodes in both lists
 # keep shifting the pointers to the next nodes until the end of the lists
 # if nodes not equal, return 0
    while llist1:
        if llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next
    return 1


tests = int(input()) # no. of test cases

for tests_itr in range(tests): # for each test case, create list1 and list2

    llist1_count = int(input()) # no. of nodes in list1
    llist1 = l.SinglyLinkedList() # creating head of list1
    for _ in range(llist1_count): # inserting the nodes of list1
        llist1_item = int(input())
        llist1.insert_node(llist1_item)

    llist2_count = int(input()) # no. of nodes in list2
    llist2 = l.SinglyLinkedList() # creating head of list2
    for _ in range(llist2_count): # inserting the nodes of list2
        llist2_item = int(input())
        llist2.insert_node(llist2_item)

    result = compare_lists(llist1.head, llist2.head)

    print(result)
