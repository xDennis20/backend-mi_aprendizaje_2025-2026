
"""
Ejercicio 1: El Validador de Seguridad (Nivel Junior)
Imagina que estás construyendo el sistema de un banco. Tienes una función delicada que transfiere dinero, pero no quieres que se ejecute si la cuenta tiene saldo negativo (números rojos).

Tu misión:

Crea un decorador llamado @verificar_saldo.

Este decorador debe inspeccionar los argumentos que recibe la función.

Si alguno de los argumentos es un número menor a 0, el decorador debe bloquear la ejecución e imprimir: "Error: Fondos insuficientes o deuda detectada".

Si todos los números son positivos, ejecuta la función normalmente.
"""
import functools


def verificar_saldo(func):
    @functools.wraps(func)
    def wraper(*args,**kwargs):
        datos_arg = args
        datos_kwargs = kwargs.values()
        for dato in datos_arg:
            if isinstance(dato, (int,float)) and dato<= 0:
                return "Error: Datos negativos"
        for dato in datos_kwargs:
            if isinstance(dato, (int,float)) <= 0:
                return "Error: Datos negativos"
        return func(*args, **kwargs)
    return wraper

@verificar_saldo
def realizar_transferencia(monto: float, saldo_actual: float):
    print(f"Transfiriendo ${monto}. Saldo restante: {saldo_actual - monto}")

print(realizar_transferencia(0,0))
print(realizar_transferencia(monto=0,saldo_actual=0))
realizar_transferencia(30,100)