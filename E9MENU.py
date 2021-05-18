from E9TEMA import *
from E9VIDEO import *
from E9CURSO_TEMA_VIDEO import *
from E9CURSO_TEMA import *
from E9CURSO import *
from E9EMPLEADO import *

print("Bienvenido a nuestra aplicación que es lo que desea guardar /n")
print("Almacenar datos de un Tema [1] /nm")
print("Almacenar datos de un Video [2] /n")
print("Almacenar datos de un Curso, Tema, Video [3] /n")
print("Almacenar datos de un Curso, Tema [4] /n")
print("Almacenar datos de un Curso [5] /n")
print("Almacenar datos de un Empleado [6] /n")
menuinicio=int(input("Introdusca el numero que desea realizar /n"))
if (menuinicio)==1:
    print("Introduzca los datos que se le piden a continuación: /n")
    RegistroTEMA= TEMA.guardar("","")
    print("Se mostrara el registro que se ha guardado /n")
    RegistroTEMA=TEMA.consultartodo("","")
    print("A continuación se buscara cualquier registro por medio del id /n")
    RegistroTEMA=TEMA.conusltarporid("")
elif (menuinicio)==2:
    print("Introduzca los datos que se le piden a continuación: /n")
    RegistroVIDEO= Video.guardar("","")
    print("Se mostrara el registro que se ha guardado /n")
    RegistroVIDEO=Video.consultartodo("","")
    print("A continuación se buscara cualquier registro por medio del id /n")
    RegistroVIDEO=Video.conusltarporid("")
elif (menuinicio)==3:
    print("Introduzca los datos que se le piden a continuación: /n")
    RegistroE9CURSO_TEMA_VIDEO= Curso_Tema_Video.guardar("","")
    print("Se mostrara el registro que se ha guardado /n")
    RegistroE9CURSO_TEMA_VIDEO=Curso_Tema_Video.consultartodo("","")
    print("A continuación se buscara cualquier registro por medio del id /n")
    RegistroE9CURSO_TEMA_VIDEO=Curso_Tema_Video.conusltarporid("")
elif (menuinicio)==4:
    print("Introduzca los datos que se le piden a continuación: /n")
    RegistroE9CURSO_TEMA= Curso_Tema.guardar("","")
    print("Se mostrara el registro que se ha guardado /n")
    RegistroE9CURSO_TEMA=Curso_Tema.consultartodo("","")
    print("A continuación se buscara cualquier registro por medio del id /n")
    RegistroE9CURSO_TEMA=Curso_Tema.conusltarporid("")
elif (menuinicio)==5:
    print("Introduzca los datos que se le piden a continuación: /n")
    RegistroE9CURSO= Curso.guardar("","")
    print("Se mostrara el registro que se ha guardado /n")
    RegistroE9CURSO=Curso.consultartodo("","")
    print("A continuación se buscara cualquier registro por medio del id /n")
    RegistroE9CURSO=Curso.conusltarporid("")
elif (menuinicio)==6:
    print("Introduzca los datos que se le piden a continuación: /n")
    RegistroE9EMPLEADO= Empleado.guardar("","")
    print("Se mostrara el registro que se ha guardado /n")
    RegistroE9EMPLEADO=Empleado.consultartodo("","")
    print("A continuación se buscara cualquier registro por medio del id /n")
    RegistroE9EMPLEADO=Empleado.conusltarporid("")
else:
    print("Digite una opción valida /n"), menuinicio