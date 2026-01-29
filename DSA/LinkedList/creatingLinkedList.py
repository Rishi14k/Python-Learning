class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

a=Node(5)
b=Node(10)
c=Node(15)

a.next = b
b.next = c
head = a
# print(head.data)
# print(head.next.data)
# print(head.next.next.data)


# this is traverse in list 
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data,end=" ")
        curr = curr.next

# printLinkedList(head)

# insertion at begnning of LL 
newNode = Node(4)
newNode.next = head
head = newNode
# printLinkedList(head)

# insertion at end of LL 
newNode2 = Node(20)

curr=head
while curr.next !=None:
    curr= curr.next

curr.next = newNode2
# printLinkedList(head)

# insertion at given position of LL 
newNode3 = Node(60)
k=3
curr1 = head
for i in range(k-1):
    curr1 = curr1.next

newNode3.next = curr1.next
curr1.next = newNode3
# printLinkedList(head)


# delete the first node

head = head.next
# printLinkedList(head)

# 3 delete the last node 
curr = head 
while curr.next.next != None:
    curr = curr.next
curr.next = None
# printLinkedList(head)

# kth node deletion
k=2
curr = head
for i in range(k-1):
    curr = curr.next
curr.next = curr.next.next
printLinkedList(head)