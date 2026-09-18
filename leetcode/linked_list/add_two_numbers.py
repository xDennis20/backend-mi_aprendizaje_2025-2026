from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    suma = 0
    acarreo = 0
    list_result = ListNode(-1)
    pointer = list_result

    while l1 or l2:
        valorl1 = l1.val if l1 else 0
        valorl2 = l2.val if l2 else 0
        suma += (valorl1 + valorl2) + acarreo
        if suma >= 10:
            pointer.next = ListNode(suma % 10)
            acarreo = suma // 10
        else:
            pointer.next = ListNode(suma)
            acarreo = 0
        suma = 0
        pointer = pointer.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next


    if acarreo == 1:
        pointer.next = ListNode(acarreo)

    return list_result.next

