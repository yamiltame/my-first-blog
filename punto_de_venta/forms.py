from django import forms
from .models import *

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        exclude=[]

class UbicacionForm(forms.ModelForm):
	class Meta:
		model= Ubicacion
		exclude=[]


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