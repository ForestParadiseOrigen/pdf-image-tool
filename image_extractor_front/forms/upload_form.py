from django import forms

class UploadForm(forms.Form):
    
    file = forms.FileField(label='Selecciona un archivo PDF.')
    
    def clean_file(self):
        file = self.cleaned_data['file']
        
        if not file.name.endswith('.pdf'):
            raise forms.ValidationError("El archivo seleccionado no es un archivo PDF.")
        return file
