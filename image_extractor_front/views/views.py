import os
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from image_extractor import settings
from ..forms.upload_form import UploadForm
from image_extractor_back.utils.process_pdf_file import extract_images_from_pdf
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage


@csrf_exempt
def upload_view(request):
    
    # Explicación: Se encarga de guardar los archivos que llegan por mediod del request.
    def save_new_file(request):
        uploaded_file = request.FILES["file"]
        if uploaded_file:
            uploaded_file_name = default_storage.save(os.path.join('uploads', 'temp', uploaded_file.name), uploaded_file)
            uploaded_file_url = default_storage.url(uploaded_file_name)
            
            extracted_images = extract_images_from_pdf(uploaded_file_url)
            
            return JsonResponse({"file_url": uploaded_file_url, "extracted_images": extracted_images})
        else:
            return JsonResponse({"error": "No se encontró ningún archivo para guardar."}, status=400)

    # Explicación: Se encarga de borrar los archivos guardados que se le especifiquen.
    def del_new_file(request):
        uploaded_file = request.FILES.get("file")
        if uploaded_file:
            uploaded_file_name = default_storage.delete(uploaded_file.name)
            if uploaded_file_name:
                print(f"El archivo {uploaded_file_name} fue eliminado.")
            else:
                print("Error al eliminar el archivo.")
        else:
            print("No se encontró ningún archivo para eliminar.")

    # Explicación: Por medio de esta sección podemos comenzar con el proceso de extracción normalmente.
    if request.method == "POST":
    
        form = UploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            return save_new_file(request)
        else:
            print("Al parecer el archivo no parece ser un PDF.")     
    else:
        form = UploadForm()
        
    return render(request, "upload_template.html", {"form": form})

    