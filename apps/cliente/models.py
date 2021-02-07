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
	tipo_documento = models.CharField('Tipo de Documento', max_length=50,primary_key=True)

	def __str__(self):
		return self.tipo

class Tramite(ModeloBase):
	tipo_tramite = models.CharField('Tipo de Servicio', max_length=50,primary_key=True)

	def __str__(self):
		return self.tipo		

class Cliente(ModeloBase):
	tipo_documento=models.ForeignKey(Documento,on_delete=models.CASCADE,null=True,blank=True)
	num_documento = models.CharField('DNI/CEDULA', max_length=10, primary_key=True)
	nombre = models.CharField('Nombres', max_length=50)
	apellido = models.CharField('Apellidos', max_length=50)
	codigo = models.IntegerField('Expediente')
	licencia = models.CharField('Licencia', max_length=50)
	fecha_inicio_licencia= models.DateField('Fecha de Expedición',null=	True,blank=	True)
	fecha_caducidad_licencia= models.DateField('Fecha de Revalidación')
	photo=models.ImageField('Foto',null=True,blank=True,upload_to='fotos/')
	empresa=models.ForeignKey(Empresa,on_delete=models.CASCADE,null=True,blank=True)
	tipo_tramite=models.ForeignKey(Tramite,on_delete=models.CASCADE,null=True,blank=True)

	class Meta:
		verbose_name='Cliente'
		verbose_name_plural='Clientes'	

	def __str__(self):
		return self.apellido	


