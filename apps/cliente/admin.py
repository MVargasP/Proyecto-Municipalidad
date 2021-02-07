from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

from import_export import resources,fields,widgets
from import_export.widgets import ForeignKeyWidget


class ClienteResource(resources.ModelResource):
    tipo_documento=fields.Field(column_name='tipo_documento',attribute='tipo_documento',widget=ForeignKeyWidget(Documento,'tipo_documento'))
    tipo_tramite=fields.Field(column_name='tipo_tramite',attribute='tipo_tramite',widget=ForeignKeyWidget(Tramite,'tipo_tramite'))
  
    def before_import_row(self, row, **kwargs):
         tipo_documento  = row.get('tipo_documento')
         tipo_tramite  = row.get('tipo_tramite')

         (doc,_created)=Documento.objects.get_or_create(tipo_documento=tipo_documento)
         (tra,_created)=Tramite.objects.get_or_create(tipo_tramite=tipo_tramite)

         
         row['tipo_documento'] = doc.tipo_documento
         row['tipo_tramite'] = tra.tipo_tramite

         
    class Meta:
        model = Cliente
        fields=('tipo_documento','num_documento','nombre','apellido','codigo','licencia',
        'fecha_inicio_licencia','fecha_caducidad_licencia','tipo_tramite') # campos que se import-export
        export_order = ['tipo_documento','num_documento','nombre','apellido',
        'codigo','licencia','fecha_inicio_licencia','fecha_caducidad_licencia','tipo_tramite']
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
        fields=('tipo_documento') # campos que se import-export
     
class DocumentoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	
	search_fields = ['tipo_documento'] # busqueda de campos
	resource_class = DocumentoResource



admin.site.register(Cliente, ClienteAdmin)
#admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Tramite)