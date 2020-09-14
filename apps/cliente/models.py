from django.db import models
from cloudinary.models import CloudinaryField

class ModeloBase(models.Model):
	
	estado = models.BooleanField('Estado', default=True)
	fecha_creacion = models.DateField('Fecha de Creacion',auto_now=False,auto_now_add=True) 
	fecha_modificacion = models.DateField('Fecha de Modificacion',auto_now=True,auto_now_add=False)
	fecha_eliminacion = models.DateField('Fecha de Eliminacion',auto_now=True,auto_now_add=False)

	class Meta:
		abstract = True

	
class Empresa(ModeloBase):
	razon_social=models.CharField('Razon razon_social',max_length=50,null=True,blank=True)
	ruc=models.CharField('Ruc Empresa',max_length=20,primary_key=True)

	class Meta:
		verbose_name='Empresa'
		verbose_name_plural='Empresas'
	def __str__(self):
		return self.razon_social

class Documento(ModeloBase):
	tipo = models.CharField('Tipo de Documento', max_length=50)

	def __str__(self):
		return self.tipo

class Tramite(ModeloBase):
	tipo = models.CharField('Tipo de Tramite', max_length=50)

	def __str__(self):
		return self.tipo		

class Cliente(ModeloBase):
	documento=models.ForeignKey(Documento,on_delete=models.CASCADE,null=True,blank=True)
	num_documento = models.CharField('DNI/CEDULA', max_length=10, primary_key=True)
	nombre = models.CharField('Nombres', max_length=50)
	apellido = models.CharField('Apellidos', max_length=50)
	codigo = models.IntegerField('Codigo')
	licencia = models.CharField('Licencia', max_length=50)
	fecha_inicio_licencia= models.DateField('Fecha de Inscripcion',null=	True,blank=	True)
	fecha_caducidad_licencia= models.DateField('Fecha de Vencimiento')
	photo=CloudinaryField('Foto de Perfil', max_length=150,null=True,blank=True)
	empresa=models.ForeignKey(Empresa,on_delete=models.CASCADE,null=True,blank=True)
	tramite=models.ForeignKey(Tramite,on_delete=models.CASCADE,null=True,blank=True)

	class Meta:
		verbose_name='Cliente'
		verbose_name_plural='Clientes'	

	def __str__(self):
		return self.apellido	


