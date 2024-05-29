from django.core.files.storage import default_storage

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
    
    