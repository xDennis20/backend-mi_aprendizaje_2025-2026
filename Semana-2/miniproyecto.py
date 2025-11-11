class Tarea:
    def __init__(self,id: int,descripcion: str,estado: bool):
        self.descripcion = descripcion
        self.id = id
        self.estado = estado

class GestorTarea:

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self):
        descripcion_tarea = input("Ingrese la descripcion de su tarea: ")
        id = len(self.tareas) + 1
        self.tareas.append(Tarea(id,descripcion_tarea,False))

    def completar_tarea(self):
        buscar_id = int(input("Ingrese el id de la tarea que desea completar: "))
        for tarea in self.tareas:
            if tarea.id == buscar_id:
                tarea.estado = True

    def eliminar_tarea(self):
        buscar_id = int(input("Ingrese el id de la tarea que desea eliminar: "))
        for tarea in self.tareas:
            if tarea.id  == buscar_id:
                self.tareas.remove(tarea)

    def mostrar_tarea(self):
        for tarea in self.tareas:
            print(f"{"[x]" if tarea.estado is True else "[]"} {tarea.id}: {tarea.descripcion}")


to_do = GestorTarea()
to_do.agregar_tarea()
to_do.agregar_tarea()
to_do.agregar_tarea()
to_do.eliminar_tarea()
to_do.mostrar_tarea()