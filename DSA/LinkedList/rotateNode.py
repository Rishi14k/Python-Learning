
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
 
def rotateNode(head,k):
    l=0
    last=head

    while last.next!=None:
        last=last.next
        l+=1
    l+=1
    k=k%l

    curr=head

    for i in range(l-k-1):
        curr=curr.next
    
    last.next=head
    head=curr.next
    curr.next =None

    return head




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

print(rotateNode(head))
print(printLinkedList(head))