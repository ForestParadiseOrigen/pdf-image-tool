import os
from django.http import JsonResponse
from image_extractor_back.utils.process_pdf_file import extract_images_from_pdf
from django.core.files.storage import default_storage

# Explicación: Se encarga de guardar los archivos que llegan por mediod del request.
def save_new_file(request):
    
    # Guarda el archivo que viene dentro del requerimiento que trae el formulario.
    uploaded_file = request.FILES["file"]
    
    # En caso de que exista un archivo dentro de la variable.
    if uploaded_file:
        
        # Procede a guardar el archivo que se cargó anteriormente y a extraér su nombre guardndolo dentro de la variable asignada.
        uploaded_file_name = default_storage.save(os.path.join(uploaded_file.name), uploaded_file)
        
        # Guarda en la variable asignada la url del archivo guardado con el nombre que se le brinda como parametro.
        uploaded_file_url = default_storage.url(uploaded_file_name)
        
        # Procede a guardar las imagenes extraidas del archivo cuya ruta se le asignó como parametro.
        extracted_images = extract_images_from_pdf(uploaded_file_url)
        
        # Muestra en el navegador la ruta del archivo que se subió y las rutas de las imagenes que se extragieron a su vez del mismo.
        return JsonResponse({"file_url": uploaded_file_url, "extracted_images": extracted_images})
    else:
        return JsonResponse({"error": "No se encontró ningún archivo para guardar."}, status=400)