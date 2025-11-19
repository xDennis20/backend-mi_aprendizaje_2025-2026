"""Problema 21: Cajero automatico
Problema: Eres un cajero automático. El usuario tiene un saldo de $1000. El usuario quiere retirar dinero, pero hay reglas:

El retiro debe ser múltiplo de 10 (no puedes dar billetes de 5 o de 1).

Si pide más de lo que tiene, debes rechazarlo.

Si pide una cantidad negativa, debes rechazarlo.

Si todo está bien, debes restar el monto y mostrar el nuevo saldo
"""
def cajero_automatico():
    saldo = 1000
    retiro = int(input("Ingrese la cantidad del retiro que desea hacer: "))
    salir = False
    while not salir:
        if retiro > saldo:
            print("Saldo insuficiente")
            salir = True
        elif retiro % 10 != 0:
            print("Se aceptan multiplos de 10")
            salir = True
        else:
            saldo-=retiro
            print(f"Retiro exitoso, saldo actual {saldo}")
            salir = True
cajero_automatico()