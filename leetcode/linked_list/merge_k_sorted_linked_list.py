from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

     def __repr__(self) -> str:
         return f"{self.val}"


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

def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    while len(lists) > 1:
        ronda_siguiente = []
        for i in range(0,len(lists) - 1,2):
            if i + 1 <= len(lists):
                l1 = lists[i]
                l2 = lists[i + 1]
                list_ordenada = merge_two_lists(l1, l2)
                ronda_siguiente.append(list_ordenada)
            else:
                ronda_siguiente.append(lists[i])
        lists = ronda_siguiente

    return lists[0]