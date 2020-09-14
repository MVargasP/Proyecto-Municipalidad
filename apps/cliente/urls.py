from django.urls import path, include
from .views import *
urlpatterns = [
	path('',ConsultaView.as_view(),name='consulta'),
	
    
 
]
