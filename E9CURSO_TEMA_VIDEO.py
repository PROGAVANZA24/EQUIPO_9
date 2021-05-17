class Curso_Tema_Video:
    def __init__(self, id_CTV, id_CT, id_video):
        self.id_CTV=id_CTV
        self.id_CT=id_CT
        self.id_video=id_video
    
    def guardar (id_CTV, id_CT, id_video):
        archivo = open ("CURSO_TEMA_VIDEO.txt", "w", enconding="ea4102e")
        id_CTV=input(int("Escribe el id del curso que deasea guardar: /n"))
        id_CT=input(int("Escribe el id del tema que deasea guardar: /n"))
        id_video=input(int("Escribe el id del video que deasea guardar: /n"))
        archivo.write("Este texto se guardara en el archivo /n")
        archivo.close ()
    
    def consultartodo(id_CTV, id_CT, id_video):
        archivo= open("CURSO_TEMA_VIDEO.txt", enconding="ea4102e")
        print(archivo.read())
        archivo.close()