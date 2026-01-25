def crear_saludador(saludo: str):
    def saludar(persona: str):
        return f"{saludo} {persona}"
    return saludar

saludar_formal = crear_saludador("Estimado/a")
saludar_casual = crear_saludador("Hola")
saludar_ingles = crear_saludador("Hello")