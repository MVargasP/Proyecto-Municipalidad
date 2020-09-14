from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from import_export import resources,fields,widgets
from import_export.admin import ImportExportModelAdmin
from .models import *
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget,ManyToManyWidget 
from django.contrib.auth.hashers import make_password
# Register your models here.
class UserResource(resources.ModelResource):
    def before_import_row(self,row, **kwargs):
           value = row['password']
           row['password'] = make_password(value)
           check_password(value)
    class Meta: 
       model = User

       fields = ('last_name', 'first_name','dni','username','password')
       export_order = ('last_name', 'first_name','dni','username','password')
       exclude = ('id', )
       import_id_fields = ['username']

       def before_import_row(self,row, **kwargs):
           value = row['password']
           row['password'] = make_password(value)
           check_password(value)
       class Meta:
           model = User
   
    	
class UserAdmin(ImportExportModelAdmin, BaseUserAdmin):
	list_display = ('username','dni')
	search_fields = ['username','dni']
	resource_class = UserResource 


#Registrar  Usuarios en el panel administrativo

admin.site.register(User, UserAdmin)
