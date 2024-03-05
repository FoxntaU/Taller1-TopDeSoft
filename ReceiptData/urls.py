from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, Data, upload_file, DetalleArchivoView, EliminarArchivoView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('data/', Data.as_view(), name='data'),
    path('createdata/', upload_file, name='createdata'),
    path('detalle_archivo/<int:archivo_id>/', DetalleArchivoView.as_view(), name='detalle_archivo'),
    path('eliminar_archivo/<int:pk>/', EliminarArchivoView.as_view(), name='eliminar_archivo'),

]
