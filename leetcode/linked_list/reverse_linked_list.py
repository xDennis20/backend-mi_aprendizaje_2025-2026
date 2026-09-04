from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    recuerdo_anterior = None
    while head is not None:
        recuerdo = head.next
        head.next = recuerdo_anterior
        recuerdo_anterior = head
        head = recuerdo

    return head
