from django import forms
from .models import *

class MarcaForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(MarcaForm, self).__init__(*args, **kwargs)

		#self.fields['nombre'].widget.attrs['class'] = 'form-control'

	class Meta:
		model = Marca
		exclude=[]

class UbicacionForm(forms.ModelForm):
	class Meta:
		model= Ubicacion
		exclude=[]
	def __init__(self,*args,**kwargs):
		super(UbicacionForm,self).__init__(*args,**kwargs)
		self.fields['municipio'].queryset=Municipio.objects.none()
		if 'estado' in self.data:
			try:
				estado_id=int(self.data.get('estado'))
				self.fields['municipio'].queryset=Municipio.objects.filter(estado_id=estado_id).order_by('nombre')
			except (ValueError,TypeError):
				pass
		elif self.instance.pk:
			self.fields['municipio'].queryset=self.instance.estado.municio_set.order_by('nombre')


class ContactoForm(forms.ModelForm):
	class Meta:
		model= Contacto
		exclude=[]

class ClienteForm(forms.ModelForm):
	class Meta:
		model= Clientes
		exclude=['ubicacion','contacto']

class ProductoForm(forms.ModelForm):
	class Meta:
		model= Productos
		exclude=[]
	def __init__(self,*args,**kwargs):
		super(ProductoForm,self).__init__(*args,**kwargs)
		self.fields["proveedores"].widget=forms.widgets.CheckboxSelectMultiple()
		self.fields["proveedores"].queryset=Proveedores.objects.all()
		self.fields["dpto"].widget=forms.widgets.CheckboxSelectMultiple()
		self.fields["dpto"].queryset=Departamento.objects.all()

class ProveedorForm(forms.ModelForm):
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
		exclude=[]