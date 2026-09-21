from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    suma = 0
    residuo = 0
    resultado = ListNode(-1)
    pointer = resultado

    while l1 or l2:
        valor_l1 = l1.val if l1 else 0
        valor_l2 = l2.val if l2 else 0

        suma += valor_l1 + valor_l2 + residuo

        if suma >= 10:
            pointer.next = ListNode(suma % 10)
            residuo = suma // 10
        else:
            pointer.next = ListNode(suma)
            residuo = 0
        suma = 0
        pointer = pointer.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if residuo == 1:
        pointer.next = ListNode(residuo)

    return resultado.next

