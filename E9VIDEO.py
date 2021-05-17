class Video:
    def __init__(self, id_video, nombre, url, fecha_publicacion):
        self.id_video=id_video
        self.nombre=nombre
        self.url=url
        self.fecha_publicacion=fecha_publicacion
    
    def guardar (id_video, nombre, url, fecha_publicacion):
        archivo = open ("VIDEO.txt", "w", enconding="343ae39")
        id_tema=input(int("Escribe el id del video que deasea guardar: /n"))
        nombre=input("Escribe el nombre del video que desea guardar: /n")
        url=input("Escribe el url del video que desea guardar: /n")
      
