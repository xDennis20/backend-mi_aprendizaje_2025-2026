import json
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
        ids = len(self.tareas) + 1
        self.tareas.append(Tarea(ids,descripcion_tarea,False))

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

    def cargar_tarea(self,archivo = "tarea.json"):
        tarea = [{"id": t.id,"descripcion": t.descripcion,"estado": t.estado} for t in self.tareas]
        with open(archivo,"w") as f:
            json.dump(tarea,f)
        print("Tareas guardado con exito")

    def cargar_archivo(self,archivo = "tarea.json"):
        try:
            with open(archivo,"r") as f:
                tareas = json.load(f)
                self.tareas = [Tarea(t["id"],t["descripcion"],t["estado"]) for t in tareas]
        except FileNotFoundError:
            self.tareas = []

to_do = GestorTarea()
to_do.agregar_tarea()
to_do.agregar_tarea()
to_do.agregar_tarea()
to_do.eliminar_tarea()
to_do.mostrar_tarea()
to_do.cargar_tarea()