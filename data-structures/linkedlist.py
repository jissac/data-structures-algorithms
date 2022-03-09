'''
# manual implementation Singly Linked List
'''

class Node():
    def __init__(self, value):
        self.val = value
        self.next = None

n1 = Node('A')
n2 = Node('B')
n3 = Node('C')

n1.next = n2
n2.next = n3

# number of nodes in linked list
def nodeTraverse(head:Node) -> int:
    count = 0
    current = head
    while current.next != None:
        print(current.val)
        count+=1
        current = current.next
    return count

print(f"Number of Nodes: {nodeTraverse(n1)}")

# reverse the nodes in linked list
def reverseLinkedList(head:Node) -> Node:
    prev = None
    current = head
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
# None      A       ->      B       ->      C
# prev      current         next
new_head = reverseLinkedList(n1)
print(f"Reversed Linked List New Head Nde: {new_head} with value: {new_head.val}")


'''
# Doubly Linked List
'''