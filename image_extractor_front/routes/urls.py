from django.urls import path
from ..views.views import upload_view

urlpatterns = [
    path('upload/', upload_view, name='upload'),
    # Otras URLs de tu aplicación...
]
