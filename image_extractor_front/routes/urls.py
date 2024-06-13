from django.urls import path
from ..views.views import upload_view
from ..views.views import deliver_files_view

urlpatterns = [
    path('upload/', upload_view, name='upload'),
    path('deliver/', deliver_files_view, name="deliver")
    # Otras URLs de tu aplicación...
]
