class Motor:
    def __init__(self, tipo: str, caballos_fuerza: int):
        if not tipo or not caballos_fuerza:
            raise ValueError("Error: Datos vacios")
        if tipo.lower() not in ("gasolina","eléctrico","híbrido"):
            raise ValueError("Error: Tipo de motor desconocido")
        self.tipo = tipo
        self.caballos_fuerza = caballos_fuerza
        self.encendido = False

    def encender(self) -> None:
        if self.encendido:
            print("El auto ya esta encendido")
            return
        self.encendido = True
        print(f"Motor {self.tipo} encendido ({self.caballos_fuerza} HP)")

    def apagar(self) -> None:
        if self.encendido:
            self.encendido = False

class Auto:
    def __init__(self, marca: str, modelo: str, motor: Motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def arrancar(self) -> None:
        self.motor.encender()
        print(f"{self.marca} {self.modelo} arrancado")

    def info(self) -> str:
        return f"{self.marca} {self.modelo} - Motor {self.motor.tipo} ({self.motor.caballos_fuerza} HP)"

# Crear motores
motor_gasolina = Motor("gasolina", 150)
motor_electrico = Motor("eléctrico", 200)

# Crear autos con composición
auto1 = Auto("Toyota", "Corolla", motor_gasolina)
auto2 = Auto("Tesla", "Model 3", motor_electrico)

# Probar
auto1.arrancar()
print(auto1.info())

auto2.arrancar()
print(auto2.info())

# Verificar estado del motor
print(f"Motor de auto1 encendido: {auto1.motor.encendido}")  # True
print(f"Motor de auto2 encendido: {auto2.motor.encendido}")  # True
