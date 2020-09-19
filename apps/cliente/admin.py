from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

from import_export import resources,fields,widgets


class ClienteResource(resources.ModelResource):
  
    class Meta:
        model = Cliente
        fields=('documento','num_documento','nombre','apellido','codigo','licencia','fecha_inicio_licencia','fecha_caducidad_licencia','empresa','tramite') # campos que se import-export
     
        import_id_fields = ['num_documento'] # import busca un id por default especificar que campo utilizare como id si cambio el pk

class ClienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('nombre','apellido','num_documento','codigo','licencia','fecha_caducidad_licencia') # campos que se mostraran
	search_fields = ['nombre','apellido','num_documento','codigo','licencia','fecha_caducidad_licencia'] # busqueda de campos
	resource_class = ClienteResource 

class EmpresaResource(resources.ModelResource):
   
    class Meta:
        model = Cliente
        fields=('ruc','razon_social') # campos que se import-export
     
class EmpresaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('ruc','razon_social') # campos que se mostraran
	search_fields = ['ruc','razon_social'] # busqueda de campos
	resource_class = EmpresaResource 

class DocumentoResource(resources.ModelResource):
   
    class Meta:
        model = Documento
        fields=('tipo') # campos que se import-export
     
class DocumentoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	
	search_fields = ['tipo'] # busqueda de campos
	resource_class = DocumentoResource



admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Tramite)