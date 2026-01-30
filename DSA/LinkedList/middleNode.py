class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

def middleNode(head):
    # curr = head
    # l=0

    # while curr != None:
    #     curr=curr.next
    #     l+=1
    
    # curr=head
    # for i in range(l//2):
    #     curr = curr.next
    
    # return curr

    slow = head
    fast = head

    while fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
    
    return slow

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

print(middleNode(head))