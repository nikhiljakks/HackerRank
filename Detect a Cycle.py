"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
pList = []
result = 1

def has_cycle(head):
    
    #print "data is " + str(head.data)
    #print "next is " + str(head.next)
    #print "head is " + str(head)
    global pList
    pList = []
    pList.append(head)
    global result
    result = 0
    def check_node(head):
        global pList
        global result
      #  print "head next is" + str(head.next)
        if (head.next is None):
       #     print "head next inside is" + str(head.next)
            result = 0
            return
        elif (head.next in pList):
            result = 1
            return
        else:
            pList.append(head.next)
            check_node(head.next)
    check_node(head)
    #print result
    return result


    
