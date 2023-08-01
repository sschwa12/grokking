class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_middle(head: Node) -> int:
    slow, fast = head, head
    while True:
        if not fast or not fast.next:
            return slow
        slow = slow.next
        fast = fast.next.next
def reverse_linked_list(head: Node) -> Node:
    prev = None
    while head.next:
        prev = head

def is_palindrome(head: Node) -> bool:
    middle = find_middle(head)

head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)
# head.next.next.next.next.next = Node(6)
# head.next.next.next.next.next.next = Node(7)

print(is_palindrome(head))
