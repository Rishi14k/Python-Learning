
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
 

def removeDuplicates(head):
    #corner case
    if head == None or head.next == None:
        return head
    
    curr=head

    while curr!=None and curr.next!=None:
        if curr.data == curr.next.data:
            curr.next=curr.next.next
        else:
            curr=curr.next
    
    return head


a=Node(5)
b=Node(5)
c=Node(10)
d=Node(10)
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

print(removeDuplicates(head))
print(printLinkedList(head))