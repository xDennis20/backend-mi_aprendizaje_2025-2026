class Estudiante:
    def __init__(self, nombre: str, id_estudiante: str):
        self.nombre = nombre
        self.id_estudiante = id_estudiante

    def __str__(self) -> str:
        return f"Estudiante: {self.nombre} (ID: {self.id_estudiante})"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(nombre='{self.nombre}, id_estudiante:'{self.id_estudiante}')"

    def __eq__(self, otro) -> bool:
        if not isinstance(otro,Estudiante):
            return NotImplemented
        return self.id_estudiante == otro.id_estudiante


class Curso:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.estudiantes : list[Estudiante] = []
        self.indice_id = {}

    def inscribir(self, estudiante: Estudiante) -> None:
        self.estudiantes.append(estudiante)
        self.indice_id[estudiante.id_estudiante] = estudiante

    def __len__(self) -> int:
        return len(self.estudiantes)

    def __getitem__(self, index: int) -> Estudiante:
        return self.estudiantes[index]

    def __contains__(self, estudiante: Estudiante) -> bool:
        return estudiante.id_estudiante in self.indice_id

    def __str__(self) -> str:
        return f"Curso {self.nombre}: {len(self.estudiantes)} estudiantes"

curso = Curso("Backend Development")
est1 = Estudiante("Ana", "EST001")
est2 = Estudiante("Luis", "EST002")

curso.inscribir(est1)
curso.inscribir(est2)

print(len(curso))  # 2
print(est1 in curso)  # True
print(curso)  # "Curso Backend Development: 2 estudiantes"