
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
 

def reverseLL(head):
    curr=head
    prev=None
    nxt=None

    while curr!=None:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    
    return prev




a=Node(5)
b=Node(10)
c=Node(15)
d=Node(20)
e=Node(24)

a.next = b
b.next = c
c.next = d
d.next = e
head = a

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data,end=" ")
        curr = curr.next

print(printLinkedList(head))

print(reverseLL(head))
print(printLinkedList(head))