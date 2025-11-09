
"""Problema 15: Validar Parentisis
Escribe una funcion que reciba un string que contiene solo los caracteres. '(',')','{','}','[',']
y determine si es valido.
Un string es valido si:
1. Cada parentesis de apertura debe tener su correspondiente parentisis de cierre
2. Los parentesis deben cerrarse en el orden correcto
3. Cada parentesis de cierre debe tener su correspondiente parentesis de apertura del mismo tipo.
Fecha: 06-11-2025"""

def validar_parentesis(signos: str) -> bool:
    aperturas = ["(","{","["]
    pares = {")": "(",
             "}": "{",
             "]": "["}
    pila_signo = []

    for signo in signos:
        if signo in aperturas:
            pila_signo.append(signo)
        else:
            if not pila_signo:
                return False
            ultimo = pila_signo.pop()
            if ultimo != pares.get(signo):
                return False
    return len(pila_signo) == 0

print(validar_parentesis("()"))
print(validar_parentesis("()[]{}"))
print(validar_parentesis("([)]"))