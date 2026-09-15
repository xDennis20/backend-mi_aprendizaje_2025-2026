from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    pointer = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            pointer.next = list1
            pointer = pointer.next
            list1 = list1.next
        else:
            pointer.next = list2
            pointer = pointer.next
            list2 = list2.next

    pointer.next = list1 or list2

    return dummy.next


