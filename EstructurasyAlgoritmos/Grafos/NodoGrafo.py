class NodoGrafo:
    def __init__(self,valor):
        self.valor = valor
        self.vecinos: dict[str,int] = {}

    def agregar_vecino(self,vecino: str, peso: int) -> None:
        self.vecinos[vecino] = peso
        print("Agregado con exito")

    def __str__(self):
        return f"Valor: {self.valor} Vecinos: {self.vecinos}"

    def __repr__(self):
        return f"{type((self)).__name__}(valor='{self.valor}', vecinos='{self.vecinos}'"