from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    pointer = dummy

    while list1 and list2:
        recuerdo_siguiente_1 = list1.next
        recuerdo_siguiente_2 = list2.next

        if list1.val <= list2.val:
            pointer.next = list1
            list1 = recuerdo_siguiente_1
        else:
            pointer.next = list2
            list2 = recuerdo_siguiente_2

        pointer = pointer.next

    if list1:
        pointer.next = list1

    elif list2:
        pointer.next = list2

    return dummy.next
