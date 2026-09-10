from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reorder_list(self, head: Optional[ListNode]) -> None:
    """Sacar la mitad de la lista enlazada"""
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    """Invertir segunda mitad"""
    segunda_mitad = slow.next
    recuerdo_anterior = None
    while segunda_mitad:
        recuerdo = segunda_mitad.next
        segunda_mitad.next = recuerdo_anterior
        recuerdo_anterior = segunda_mitad
        segunda_mitad = recuerdo

    """Unir las 2 listas separadas"""
    slow.next = None
    segunda_mitad = recuerdo_anterior
    primera_mitad = head
    while segunda_mitad:
        recuerdo_primero = primera_mitad.next
        recuerdo_segundo = segunda_mitad.next
        primera_mitad.next = segunda_mitad
        segunda_mitad.next = recuerdo_primero
        primera_mitad =recuerdo_primero
        segunda_mitad = recuerdo_segundo