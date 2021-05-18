class Curso:
    def __init__(self, id_curso, descripcion, id_empleado):
        self.id_curso=id_curso
        self.descripcion=descripcion
        self.id_empleado=id_empleado
    
    def guardar (id_curso, descripcion, id_empleado):
        archivo = open ("CURSO.txt", "w", enconding="6328e15")
        id_curso=input(int("Escribe el id del curso que deasea guardar: /n"))
        descripcion=input("Escribe la descricion del curso que deasea guardar: /n")
        id_empleado=input(int("Escribe el id del empleado que deasea guardar: /n"))
        archivo.write("Este texto se guardara en el archivo /n")
        archivo.close ()
    
    def consultartodo(id_curso, descripcion, id_empleado):
        archivo= open("CURSO.txt", enconding="6328e15")
        print(archivo.read())
        archivo.close()

    def conusltarporid(id_curso):
        archivo=open("CURSO.txt", enconding="6328e15")
        for linea in archivo:
            id_curso= linea.strip().split("|")
            print(f'{id_curso[0]:<40}{float(id_curso[1]):>10,.2f}')
        archivo.close()