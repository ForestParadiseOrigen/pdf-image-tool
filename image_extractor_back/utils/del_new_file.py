import shutil
import os

def del_new_file(uploaded_file, extracted_images):
    try:
        # Verificar si la carpeta subida existe
        if os.path.exists(uploaded_file):
            print(f'Eliminando la carpeta: {uploaded_file}')
            shutil.rmtree(str(uploaded_file))
            print(f'Se ha eliminado la carpeta y su contenido: {uploaded_file}')
        else:
            print(f'La carpeta no existe: {uploaded_file}')
        
        # Verificar y eliminar cada imagen extraída
        for image in extracted_images:
            if os.path.exists(image):
                print(f'Eliminando la imagen: {image}')
                os.remove(str(image))
                print(f'Se ha eliminado la imagen: {image}')
            else:
                print(f'La imagen no existe: {image}')

    except Exception as e:
        print(f'Error al intentar eliminar la carpeta o imágenes: {e}')
