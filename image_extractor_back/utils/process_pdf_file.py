import os
import fitz
from django.conf import settings

from image_extractor_back.utils.del_new_file import del_new_file

def extract_images_from_pdf(uploaded_file_url):
    
    # Inicializar el documento PDF 
    pdf_document = fitz.open(uploaded_file_url)
    
    if not pdf_document:
        print(f"No se ha encontrado el archivo PDF especificado en la ruta: {uploaded_file_url}")

    images = []
    
    # Recorrer todas las páginas del PDF
    for page_number in range(len(pdf_document)):
        # Obtener la página actual
        page = pdf_document[page_number]
        # Obtener la lista de imágenes incrustadas en la página
        image_list = page.get_images(full=True)
        # Recorrer cada imagen en la lista de imágenes
        for img_index, img in enumerate(image_list):
            # Obtener la imagen y guardarla en la lista
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            
            # Crear un nombre de archivo único para cada imagen
            image_filename = f"image_page{page_number+1}_img{img_index+1}.png"
            image_filepath = os.path.join(settings.MEDIA_ROOT, image_filename)

            # Guardar la imagen en el sistema de archivos
            with open(image_filepath, "wb") as image_file:
                image_file.write(image_bytes)
                
            # Agregar la ruta de la imagen guardada a la lista
            images.append(image_filepath)
            
            print(f"Imagen guardada: {image_filepath}")
    
    # Cerrar el documento PDF
    pdf_document.close()

    return images
                                                                       