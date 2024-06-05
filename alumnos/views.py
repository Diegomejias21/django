from django.shortcuts import render

from .models import Genero,Alumno
# Create your views here.

def index(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos":alumnos}
    return render(request,"alumnos/index.html",context)

def crud(request):
    alumnos = alumnos.objects.all()
    context = {'alumnos' : alumnos}
    return render(request, 'alumnos/alumnos_list.html',context)

def alumnos_add(request):
    if request.method is not "POST":
        #no es un POST, por lo tanto se muestra el formulario para agregar.
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request,"alumnos/alumnos_add.html",context)
    
    else:
        #ES un POST, por lo tanto se recuperan los datos del formulario
        #y se graban en la tabla.
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)
        obj=Alumno.objects.create( rut=rut,
                                    nombre=nombre,
                                    apellido_paterno=aPaterno,
                                    apellido_materno=aMaterno,
                                    fecha_nacimiento=fechaNac,
                                    id_genero=objGenero,
                                    telefono=telefono,
                                    email=email,
                                    direccion=direccion,
                                    activo=1 )
        obj.save()
        context={'mensaje ': "OK, datos grabados...."}
        return render(request,"alumnos/alumnos_add.html",context)
        
def alumnos_edit(request):
    context={}
    return render(request,"alumnos/alumnos_edit.html",context)

def alumnos_list(request):
    context={}
    return render(request,"alumnos/alumnos_list.html",context)


# def listadoSQL(request):
#     alumnos = Alumno.objects.raw('SELECT * FROM alumnos_alumno')
#     print(alumnos)
#     context = { "alumnos":alumnos }
#     return render(request,"alumnos/listadoSQL.html", context)