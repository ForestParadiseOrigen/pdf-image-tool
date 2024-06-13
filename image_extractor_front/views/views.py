from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ..forms.upload_form import UploadForm

from image_extractor_back.utils.save_new_file import save_new_file
# from image_extractor_back.utils.del_new_file import del_new_file

@csrf_exempt
def upload_view(request):

    # Explicación: Por medio de esta sección podemos comenzar con el proceso de extracción normalmente.
    if request.method == "POST":
        
        # Encargado de comprobar que el archivo que llega en el requerimiento del formulario contiene un archivo PDF.
        form = UploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Método encargado de guardar los archivos en el backend del proyecto.
            save_file = save_new_file(request)  
            return save_file
        else:
            print("Al parecer el archivo no parece ser un PDF.")     
    else:
        form = UploadForm()
        
    return render(request, "upload_template.html", {"form": form})

@csrf_exempt
def deliver_files_view(request):
    # Explicación: Por medio de esta sección se van a mostrar todos los archivos que están almacenados en la carpeta uploads.
    return render(request, "deliver_files.html")


# Pendiente: Hay que realizar una mejor gestión de las vistas, me refiero a hacerlas visualmente atractivas.