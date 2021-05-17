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
    
    def conusltarporid(id_tema):
        archivo=open("TEMA.txt", enconding="63da2cf")
        for linea in archivo:
            id_tema= linea.strip().split("|")
            print(f'{id_tema[0]:<40}{float(id_tema[1]):>10,.2f}')
        archivo.close()
