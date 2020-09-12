from django.db import models
from cloudinary.models import CloudinaryField

class ModeloBase(models.Model):
	
	estado = models.BooleanField('Estado', default=True)
	fecha_creacion = models.DateField('Fecha de Creacion',auto_now=False,auto_now_add=True) 
	fecha_modificacion = models.DateField('Fecha de Modificacion',auto_now=True,auto_now_add=False)
	fecha_eliminacion = models.DateField('Fecha de Eliminacion',auto_now=True,auto_now_add=False)

	class Meta:
		abstract = True

class Cliente(ModeloBase):
	dni = models.CharField('DNI', max_length=10, primary_key=True)
	nombre = models.CharField('Nombres', max_length=50)
	apellido = models.CharField('Apellidos', max_length=50)


	class Meta:
		verbose_name='Cliente'
		verbose_name_plural='Clientes'		