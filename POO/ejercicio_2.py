"""EJERCICIO 2: "Validador de Datos HTTP" (1.5 horas)
Contexto: En Backend, recibirás datos JSON. Necesitas validarlos antes de guardarlos.
Requisitos:
Crea una clase ValidadorUsuario que valide datos de usuarios:

Atributos:
errores (lista vacía al inicio)


Método validar(datos):

datos es un diccionario: {"nombre": "...", "edad": ..., "email": "..."}
Valida:

Nombre: No vacío, mínimo 3 caracteres
Edad: Entre 18 y 100
Email: Debe contener "@"


Si hay errores, agrégalos a self.errores
Retorna True si no hay errores, False si los hay


Método obtener_errores():

Retorna la lista de errores"""

class ValidadorUsuario:
    def __init__(self):
        self.errores = []

    def validar(self,datos: dict) -> bool:
        self.errores = []
        if not datos:
            return True
        nombre = datos.get("nombre","").strip()
        email = datos.get("email","")
        edad = datos.get("edad",0)
        if not nombre or len(nombre) < 3:
            self.errores.append("Error: El campo 'nombre' no cumple con la longitud de caracteres requeridas")
        if not (18 <= edad <= 100):
            self.errores.append("Error: La edad no esta en el rango requerido (18-100)")
        if "@" not in email :
            self.errores.append("Error: El email no es valido, no contiene el '@'")
        return len(self.errores) == 0

    def obtener_errores(self) -> list[str]:
        return self.errores

validador = ValidadorUsuario()

# Test 1: Datos inválidos
validador = ValidadorUsuario()
resultado = validador.validar({"nombre": "Jo", "edad": 150, "email": "sin_arroba"})
print(resultado)  # False
print(validador.obtener_errores())  # Debe listar 3 errores

# Test 2: Datos válidos con NUEVO validador
validador2 = ValidadorUsuario()
resultado2 = validador2.validar({"nombre": "Juan", "edad": 25, "email": "juan@example.com"})
print(resultado2)  # True
print(validador2.obtener_errores())  # [] (lista vacía)

# Test 3: El validador original mantiene sus errores
print(validador.obtener_errores())  # Debe seguir con los 3 errores del Test 1

print("\n=== Test 5: Datos faltantes (sin keys) ===")
v = ValidadorUsuario()
resultado = v.validar({})  # Diccionario vacío
print(f"Resultado: {resultado}")  # False
print(f"Errores: {v.obtener_errores()}")  # Debe tener 3 errores

print("\n=== Test 6: Nombre con espacios ===")
v2 = ValidadorUsuario()
resultado = v2.validar({"nombre": "   ", "edad": 25, "email": "test@test.com"})
print(f"Resultado: {resultado}")  # False
print(f"Errores: {v2.obtener_errores()}")  # Debe detectar nombre inválido

print("\n=== Test 7: Reusar instancia ===")
v3 = ValidadorUsuario()
v3.validar({"nombre": "A", "edad": 10, "email": "noarroba"})  # 3 errores
print(f"Primera validación: {v3.obtener_errores()}")
v3.validar({"nombre": "Juan", "edad": 25, "email": "juan@test.com"})  # 0 errores
print(f"Segunda validación: {v3.obtener_errores()}")  # Debe estar vacía []