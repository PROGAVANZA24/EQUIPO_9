class Empleado:
    def __init__(self, id_empleado, nombre, direccion):
        self.id_empleado=id_empleado
        self.nombre=nombre
        self.direccion=direccion
    
    def guardar (id_empleado, nombre, direccion):
        archivo = open ("CURSO.txt", "w", enconding="6328e15")
        id_empleado=input(int("Escribe el id del empleado que deasea guardar: /n"))
        nombre=input("Escribe el nombre del empleado que deasea guardar: /n")
        direccion=input("Escribe la direccion del empleado que deasea guardar: /n")