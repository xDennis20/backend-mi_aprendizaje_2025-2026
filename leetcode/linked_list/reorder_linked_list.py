from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reorder_list(head: Optional[ListNode]) -> None:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    segunda_mitad = slow.next
    slow.next = None

    """Invertir la lista"""
    recuerdo_anterior = None
    while segunda_mitad:
        recuerdo_siguiente = segunda_mitad.next
        segunda_mitad.next = recuerdo_anterior
        recuerdo_anterior = segunda_mitad
        segunda_mitad = recuerdo_siguiente

    """Unir las 2 listas"""
    segunda_mitad = recuerdo_anterior
    primera_mitad = head
    while segunda_mitad:
        recuerdo_siguiente_1 = primera_mitad.next
        recuerdo_siguiente_2 = segunda_mitad.next

        primera_mitad.next = segunda_mitad
        segunda_mitad.next = recuerdo_siguiente_1

        primera_mitad = recuerdo_siguiente_1
        segunda_mitad = recuerdo_siguiente_2
