class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_middle(head: Node) -> int:
    slow, fast = head, head
    while True:
        if not fast or not fast.next:
            return slow.value
        slow = slow.next
        fast = fast.next.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)

print(find_middle(head))
