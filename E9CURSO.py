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
      