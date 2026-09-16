from typing import Optional

class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    nodos: dict[Node,Node] = {}
    pointer = head

    while pointer:
        nodos[pointer] = Node(pointer.val)
        pointer = pointer.next

    pointer = head

    while pointer:
        nodos[pointer].next = nodos.get(pointer.next, None)
        nodos[pointer].random = nodos.get(pointer.random, None)
        pointer = pointer.next

    return nodos[head]