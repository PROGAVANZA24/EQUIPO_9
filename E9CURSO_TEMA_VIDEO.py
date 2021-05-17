class Curso_Tema_Video:
    def __init__(self, id_CTV, id_CT, id_video):
        self.id_CTV=id_CTV
        self.id_CT=id_CT
        self.id_video=id_video
    
    def guardar (id_CTV, id_CT, id_video):
        archivo = open ("VIDEO.txt", "w", enconding="343ae39")
        id_CTV=input(int("Escribe el id del curso que deasea guardar: /n"))
        id_CT=input(int("Escribe el id del tema que deasea guardar: /n"))
        id_video=input(int("Escribe el id del video que deasea guardar: /n"))
        