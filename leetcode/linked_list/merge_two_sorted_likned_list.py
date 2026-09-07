from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    current_pointer = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current_pointer.next = list1
            list1 = list1.next
        else:
            current_pointer.next = list2
            list2 = list2.next
        current_pointer = current_pointer.next

    if list1:
        current_pointer.next = list1
    elif list2:
        current_pointer.next = list2

    return dummy.next


