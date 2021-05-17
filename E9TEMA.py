class TEMA:
    def __init__(self, id_tema, nombre):
        self.id_tema=id_tema
        self.nombre=nombre
    
    def guardar (id_tema, nombre):
        archivo = open ("TEMA.txt", "w", enconding="63da2cf")
        id_tema=input(int("Escribe el id del tema que deasea guardar: /n"))
        nombre=input("Escribe el nombre del tema que desea guardar: /n")
        archivo.write("Este texto se guardara en el archivo: /n")
        archivo.close ()
    
    def consultartodo(id_tema, nombre):
        archivo= open("TEMA.txt", enconding="63da2cf")
        print(archivo.read())
        archivo.close()
    
    
