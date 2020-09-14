from django.urls import path, include
from .views import *
urlpatterns = [
	path('consulta',ConsultaView.as_view())
    
 
]
