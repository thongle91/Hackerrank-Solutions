"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    node = Node(data, None)
    if head is None:
        head = node
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = Node(data, None)
    
    return head