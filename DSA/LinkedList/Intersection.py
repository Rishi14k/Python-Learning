
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

def getLength(head):
    l=0
    curr=head
    while curr!=None:
        curr=curr.next
        l+=1
    return l

# def interSection(head1,head2):
#     len1 = getLength(head1)
#     len2 = getLength(head2)

#     if len1>len2:
#         diff=len1-len2
#         for _ in range(diff):
#             head1=head1.next
#     else:
#         diff=len2-len1
#         for _ in range(diff):
#             head2=head2.next
    
#     while head1 and head2:
#         if head1==head2:
#             return head1

#         head1=head1.next
#         head2=head2.next
    
#     return None

def interSection(head1,head2):
    p1=head1
    p2=head2
    c=0

    while True:
        if p1==p2:
            return p1

        p1=p1.next
        p2=p2.next

        if p2==None:
            p2=head1
            c+=1
        if p1==None:
            p1=head2

        if c>1:
            return None


a=Node(5)
b=Node(6)
c=Node(7)
d=Node(8)
e=Node(9)
f=Node(10)

g=Node(15)
h=Node(20)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
head1 = a

g.next = h
h.next = d
d.next = e
e.next = f
head2=g

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data,end=" ")
        curr = curr.next


print(interSection(head1,head2))

print(printLinkedList(head1))
print(printLinkedList(head2))
