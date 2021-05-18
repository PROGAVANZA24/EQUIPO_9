class Curso_Tema:
    def __init__(self, id_CT, id_curso, id_tema):
        self.id_CT=id_CT
        self.id_curso=id_curso
        self.id_tema=id_tema
    def guardar (id_CT, id_curso, id_tema):
        archivo = open ("CURSO_TEMA.txt", "w", enconding="ea4102e")
        id_CT=input(int("Escribe el id del curso del tema que deasea guardar: /n"))
        id_curso=input(int("Escribe el id del curso que deasea guardar: /n"))
        id_tema=input(int("Escribe el id del tema que deasea guardar: /n"))
        archivo.write("Este texto se guardara en el archivo /n")
        archivo.close ()

    def consultartodo(id_CT, id_curso, id_tema):
        archivo= open("CURSO_TEMA.txt", enconding="ea4102e")
        print(archivo.read())
        archivo.close()

    def conusltarporid(id_CT):
        archivo=open("CURSO_TEMA.txt", enconding="ea4102e")
        for linea in archivo:
            id_CT= linea.strip().split("|")
            print(f'{id_CT[0]:<40}{float(id_CT[1]):>10,.2f}')
        archivo.close()
