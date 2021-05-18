class Empleado:
    def __init__(self, id_empleado, nombre, direccion):
        self.id_empleado=id_empleado
        self.nombre=nombre
        self.direccion=direccion
    
    def guardar (id_empleado, nombre, direccion):
        archivo = open ("EMPLEADO.txt", "w", enconding="6328e15")
        id_empleado=input(int("Escribe el id del empleado que deasea guardar: /n"))
        nombre=input("Escribe el nombre del empleado que deasea guardar: /n")
        direccion=input("Escribe la direccion del empleado que deasea guardar: /n")
        archivo.write("Este texto se guardara en el archivo /n")
        archivo.close ()
    
    def consultartodo(id_empleado, nombre, direccion):
        archivo= open("EMPLEADO.txt", enconding="6328e15")
        print(archivo.read())
        archivo.close()

    def conusltarporid(id_empleado):
        archivo=open("EMPLEADO.txt", enconding="6328e15")
        for linea in archivo:
            id_empleado= linea.strip().split("|")
            print(f'{id_empleado[0]:<40}{float(id_empleado[1]):>10,.2f}')
        archivo.close()