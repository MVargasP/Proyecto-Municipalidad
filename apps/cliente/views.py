from django.shortcuts import render,redirect, get_object_or_404 
from django.views.generic import ListView, DetailView, View,TemplateView
from .models import Cliente,Empresa

class ConsultaView(ListView):
	model=Cliente
	
	def post(self,request,*args,**kwargs):
		buscar= request.POST['buscalo']
		dni= Cliente.objects.filter(num_documento__exact=buscar)
		empresa=Empresa.objects.filter(estado=True)
		
		contexto = {	
			'dni':dni,
			'empresa':empresa,
			'busqueda':buscar
		}
		
		return render(request,'cliente/cliente_list.html',contexto)