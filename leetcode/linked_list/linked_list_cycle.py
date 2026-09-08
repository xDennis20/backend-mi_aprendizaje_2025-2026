from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def has_cycle(head: Optional[ListNode]) -> bool:
    tortuga: ListNode = head
    liebre: ListNode = head

    while liebre and liebre.next:
        liebre = liebre.next.next
        tortuga = tortuga.next
        if liebre == tortuga:
            return True
    return False