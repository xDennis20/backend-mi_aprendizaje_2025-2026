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
        id_tarea = len(self.tareas) + 1
        self.tareas.append(Tarea(id_tarea, descripcion_tarea, False))

    def completar_tarea(self):
        try:
            buscar_id = int(input("Ingrese el id de la tarea que desea completar: "))
            for tarea in self.tareas:
                if tarea.id == buscar_id:
                    tarea.estado = True
                    return
            print("ID no encontrado.")
        except ValueError:
            print("Entrada invalida: debe ser un numero entero")
    def eliminar_tarea(self):
        buscar_id = int(input("Ingrese el id de la tarea que desea eliminar: "))
        for tarea in self.tareas:
            if tarea.id  == buscar_id:
                self.tareas.remove(tarea)

    def mostrar_tarea(self):
        for tarea in self.tareas:
            print(f"{"[x]" if tarea.estado is True else "[]"} {tarea.id}: {tarea.descripcion}")

    def guardar_tarea_json(self,archivo = "tarea.json"):
        tarea = [{"id": t.id,"descripcion": t.descripcion,"estado": t.estado} for t in self.tareas]
        with open(archivo,"w") as f:
            json.dump(tarea,f)
        print("Tareas guardadas con exito")

    def cargar_archivo(self,archivo = "tarea.json"):
        try:
            with open(archivo,"r") as f:
                datos = json.load(f)
                self.tareas = [Tarea(t["id"],t["descripcion"],t["estado"]) for t in datos]
        except FileNotFoundError:
            self.tareas = []

def main():
    salir = False
    print("¡Bienvenido a To-do!")
    gestor_tarea = GestorTarea()
    gestor_tarea.cargar_archivo()
    while not salir:
        print("\nSistema To-do")
        print("1. Agregar tarea")
        print("2. Mostrar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = int(input("Escoja una opcion 1-5: "))
        match opcion:
            case 1:
                gestor_tarea.agregar_tarea()
                gestor_tarea.guardar_tarea_json()
            case 2:
                gestor_tarea.mostrar_tarea()
            case 3:
                gestor_tarea.completar_tarea()
                gestor_tarea.guardar_tarea_json()
            case 4:
                gestor_tarea.eliminar_tarea()
                gestor_tarea.guardar_tarea_json()
            case 5:
                print("Saliendo del sistema")
                salir = True
            case _:
                print("Opcion incorrecta")
main()