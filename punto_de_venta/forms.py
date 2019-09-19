# -*- coding: utf-8 -*-
from django import forms
from .models import *
from .validators import *
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

class MarcaForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(MarcaForm, self).__init__(*args, **kwargs)

		#self.fields['nombre'].widget.attrs['class'] = 'form-control'

	class Meta:
		model = Marca
		exclude=[]

class UbicacionForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(UbicacionForm,self).__init__(*args,**kwargs)
		self.fields['codigo_postal'].validators=[RegexValidator(r'^\d{5}$',message='Codigo postal invalido')]
		self.fields['municipio'].queryset=Municipio.objects.none()
		if 'estado' in self.data:
			try:
				estado_id=int(self.data.get('estado'))
				self.fields['municipio'].queryset=Municipio.objects.filter(estado_id=estado_id).order_by('nombre')
			except (ValueError,TypeError):
				pass
		elif self.instance.pk:
			self.fields['municipio'].queryset=self.instance.estado.municipio_set.order_by('nombre')

	class Meta:
		model= Ubicacion
		exclude=[]
	


class ContactoForm(forms.ModelForm):
	class Meta:
		model= Contacto
		exclude=[]

class ClienteForm(forms.ModelForm):

	giro=forms.CharField( required=False, label="Giro.", max_length=100)

	def __init__(self,*args,**kwargs):
		super(ClienteForm,self).__init__(*args,**kwargs)
		self.fields['rfc']=forms.CharField( required=True, label="Registro tributario", max_length=13, min_length=12)
		if args and len(args[0]['rfc']) == 12: 
			self.fields['giro'].required=True
			self.fields['rfc'].validators=[self.valida_rfc_moral]
		elif args:
			self.fields['rfc'].validators=[self.valida_rfc_fisica]
	

	def valida_rfc_moral(self,valor):
		chk=True
		for l in valor[9:12]:
			chk= chk and (l.isalpha() or l.isdigit())
		if not (valor[0:3].isalpha() and valor[3:9].isdigit() and chk):
			raise ValidationError(
				_('RFC de persona moral deben ser 3 letras, 6 numeros y 3 alfanumericos'),
			)

	def valida_rfc_fisica(self,valor):
		chk=True
		for l in valor[10:13]:
			chk= chk and (l.isalpha() or l.isdigit())
		if not (valor[0:4].isalpha() and valor[4:10].isdigit() and chk):
			raise ValidationError(
				_('RFC de persona fisica deben ser 4 letras, 6 numeros y 3 alfanumericos'),
			)
	class Meta:
		model= Clientes
		exclude=['ubicacion','contacto']


class ProductoForm(forms.ModelForm):
	class Meta:
		model= Productos
		exclude=[]

class Productomarcaform(forms.ModelForm):
	class Meta:
		model=Productos
		fields=['marca']
#	def __init__(self,*args,**kwargs):
#		super(Productomarcaform,self).__init__(*args,**kwargs)
#		self.fields['marca'].widget.attrs['class']='selectpicker'

class Productodptoform(forms.ModelForm):
	class Meta:
		model=Productos
		fields=['dpto']

class Productomedidaform(forms.ModelForm):
	class Meta:
		model=Productos
		fields=['medida']

class Productoproveedorform(forms.ModelForm):
	class Meta:
		model=Productos
		fields=['proveedores']

class ProveedorForm(forms.ModelForm):

	giro=forms.CharField( required=False, label="Giro.", max_length=100)

	def __init__(self,*args,**kwargs):
		super(ProveedorForm,self).__init__(*args,**kwargs)
		self.fields['rfc']=forms.CharField( required=True, label="Registro tributario", max_length=13, min_length=12)
		if args and len(args[0]['rfc']) == 12: 
			self.fields['giro'].required=True
			self.fields['rfc'].validators=[RegexValidator(r'^[A-Z]{3}\d{6}[\dA-Z]{3}$',message='Rfc moral invalido')]
		elif args:
			self.fields['rfc'].validators=[RegexValidator(r'^[A-Z]{4}\d{6}[\dA-Z]{3}$',message='Rfc fisico invalido')]
	class Meta:
		model= Proveedores
		exclude=['ubicacion','contacto']

class MedidaForm(forms.ModelForm):
	class Meta:
		model = Medidas
		exclude=[]

class DepartamentoForm(forms.ModelForm):
	class Meta:
		model = Departamento
		exclude=[]

class DetalleVentaForm(forms.ModelForm):
	class Meta:
		model=Detalle_Venta
		exclude=['venta']

class VentaForm(forms.ModelForm):
	class Meta:
		model=Ventas
		exclude=['caja']

class CajaOperacionForm(forms.ModelForm):
	class Meta:
		model=Caja_operacion
		exclude=[]

class CajaOperacionCajaForm(forms.ModelForm):
	class Meta:
		model=Caja_operacion
		fields=['caja']

class intervaloform(forms.Form):
	opciones=[('i','intervalo'),('a','año'),('m','mes'),('d','dia')]
	visualizacion=forms.ChoiceField(label='Visualizacion',choices=opciones)
	inicio=forms.DateTimeField(label='Inicio',help_text="YYYY-MM-DD")
	fin=forms.DateTimeField(label='Fin')