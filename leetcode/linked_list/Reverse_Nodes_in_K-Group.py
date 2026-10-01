from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(-1)
    dummy.next = head
    grupo_prev = dummy
    nodo_explorador = dummy

    while True:
        for _ in range(k):
            nodo_explorador = nodo_explorador.next
            if nodo_explorador is None:
                break
        if nodo_explorador is None:
            break
        grupo_sig = nodo_explorador.next
        cabeza_original = grupo_prev.next
        curr = grupo_prev.next
        recuerdo_anterior = grupo_sig
        while curr != grupo_sig:
            recuerdo = curr.next
            curr.next = recuerdo_anterior
            recuerdo_anterior = curr
            curr = recuerdo
        grupo_prev.next = recuerdo_anterior
        grupo_prev = cabeza_original

        nodo_explorador = grupo_prev

    return dummy.next