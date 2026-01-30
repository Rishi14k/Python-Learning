class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    

def removeNode(head,n):
    # l=0
    # curr = head 

    # while curr !=None:
    #     curr=curr.next
    #     l+=1
    
    # iteration = l-(n+1)

    # curr=head
    # for i in range(iteration):
    #     curr=curr.next

    # curr.next = curr.next.next

    # return head

    p1=head
    p2=head

    for i in range(n):
        p2=p2.next
    if p2 == None:
        head=head.next
        return head
    
    while p2.next!=None:
        p2=p2.next
        p1=p1.next

    p1.next = p1.next.next
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

print(removeNode(head,3))   

printLinkedList(head)