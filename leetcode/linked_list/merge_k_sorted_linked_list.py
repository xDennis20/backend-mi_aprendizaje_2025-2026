from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    while len(lists) > 1:
        maximo = len(lists)
        ronda_siguiente = []
        for i in range(0,maximo,2):
            if i + 1 <= maximo:
                l1 = lists[i]
                l2 = lists[i + 1]
                dummy = ListNode(-1)
                pointer = dummy

                while l1 and l2:
                    recuerdo_siguiente_1 = l1.next
                    recuerdo_siguiente_2 = l2.next

                    if l1.val <= l2.val:
                        pointer.next = l1
                        l1 = recuerdo_siguiente_1
                    else:
                        pointer.next = l2
                        l2 = recuerdo_siguiente_2

                    pointer = pointer.next

                if l1:
                    pointer.next = l1
                elif l2:
                    pointer.next = l2

                ronda_siguiente.append(dummy.next)
            else:
                ronda_siguiente.append(lists[i])

        lists = ronda_siguiente

    return lists