class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

def deleteNode(node):
    node.data = node.next.data
    node.next = node.next.next

    return node

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

print(deleteNode(c))