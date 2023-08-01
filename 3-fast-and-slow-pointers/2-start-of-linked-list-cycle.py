class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def get_cycle_length(slow):
    current = slow
    l = 0
    while True:
        current = current.next
        l += 1
        if current == slow:
            return l


def start_of_cycle(head):
    k = 0
    slow, fast = head, head
    while not fast or not fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
          current = slow
          while True:
              current = current.next
              k += 1
              if current == slow:
                  break
          break
    print(k)
    


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

start_of_cycle(head)