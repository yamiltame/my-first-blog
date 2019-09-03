from .models import *
from forms import *

diccionario={
	'marca':{'marca':None},
	'medida':{'medida':None},
	'departamento':{'departamento':None},
}

#OBTENER CATALOGOS-----------
def CMarca():
	return Marca.objects.all()
def CProducto():
	return Productos.objects.all()
def CCliente():
	return Clientes.objects.all()
def CProveedor():
	return Proveedores.objects.all()
def CMedida():
	return Medidas.objects.all()
def CDepartamento():
	return Departamento.objects.all()
def CUbicacion():
	return Ubicacion.objects.all()
def CContacto():
	return Contacto.objects.all()

def get_catalogo(tipo):
	D={
		'marca': CMarca,
		'producto': CProducto,
		'cliente': CCliente,
		'proveedor':CProveedor,
		'medida': CMedida,
		'departamento': CDepartamento,
		'ubicacion': CUbicacion,
		'contacto': CContacto
		}
	func=D.get(tipo, lambda: "no existe tipo")
	return func()
#-------------------

#obtener elemento------------------------
def EMarca(pk):
	return Marca.objects.get(pk=pk)
def EProducto(pk):
	return Productos.objects.get(pk=pk)
def ECliente(pk):
	return Clientes.objects.get(pk=pk)
def EProveedor(pk):
	return Proveedores.objects.get(pk=pk)
def EMedida(pk):
	return Medidas.objects.get(pk=pk)
def EDepartamento(pk):
	return Departamento.objects.get(pk=pk)
def EUbicacion(pk):
	return Ubicacion.objects.get(pk=pk)
def EContacto(pk):
	return Contacto.objects.get(pk=pk)

def get_E(tipo,pk):
	D={
		'marca': EMarca,
		'producto': EProducto,
		'cliente': ECliente,
		'proveedor': EProveedor,
		'medida': EMedida,
		'departamento': EDepartamento,
		'ubicacion': EUbicacion,
		'contacto': EContacto
		}
	func=D.get(tipo, lambda: "no existe tipo")
	return func(pk)
#------------------------------------------

#obtener formulario editar ------------------
def FeMarca(request,qs):
	return MarcaForm(request.POST,instance=qs)
def FeProducto(request,qs):
	return ProductoForm(request.POST,instance=qs)
def FeCliente(request,qs):
	return ClienteForm(request.POST,instance=qs)
def FeProveedor(request,qs):
	return ProveedorForm(request.POST,instance=qs)
def FeMedida(request,qs):
	return MedidaForm(request.POST,instance=qs)
def FeDepartamento(request,qs):
	return DepartamentoForm(request.POST,instance=qs)
def FeUbicacion(request,qs):
	return UbicacionForm(request.POST,instance=qs)
def FeContacto(request,qs):
	return ContactoForm(request.POST,instance=qs)

def get_Fe(tipo,request,qs):
	D={
		'marca': FeMarca,
		'producto': FeProducto,
		'cliente': FeCliente,
		'proveedor': FeProveedor,
		'medida': FeMedida,
		'departamento': FeDepartamento,
		'ubicacion': FeUbicacion,
		'contacto': FeContacto
		}
	func=D.get(tipo, lambda: "no existe tipo")
	return func(request,qs)
#-------------------------------------------------

#obtenerformulario post-------------------------
def FpMarca(request):
	return MarcaForm(request.POST)
def FpProducto(request):
	return ProductoForm(request.POST)
def FpCliente(request):
	return ClienteForm(request.POST)
def FpProveedor(request):
	return ProveedorForm(request.POST)
def FpMedida(request):
	return MedidaForm(request.POST)
def FpDepartamento(request):
	return DepartamentoForm(request.POST)
def FpUbicacion(request):
	return UbicacionForm(request.POST)
def FpContacto(request):
	return ContactoForm(request.POST)

def get_Fp(tipo,request):
	D={
		'marca': FpMarca,
		'producto': FpProducto,
		'cliente': FpCliente,
		'proveedor': FpProveedor,
		'medida': FpMedida,
		'departamento': FpDepartamento,
		'ubicacion': FpUbicacion,
		'contacto': FpContacto
		}
	func=D.get(tipo, lambda: "no existe tipo")
	return func(request)
#--------------------------------------------------

#obtener formulario vacio------------------------------
def FMarca():
	return MarcaForm()
def FProducto():
	return ProductoForm()
def FCliente():
	return ClienteForm()
def FProveedor():
	return ProveedorForm()
def FMedida():
	return MedidaForm()
def FDepartamento():
	return DepartamentoForm()
def FUbicacion():
	return UbicacionForm()
def FContacto():
	return ContactoForm()

def get_F(tipo):
	D={
		'marca': FMarca,
		'producto': FProducto,
		'cliente': FCliente,
		'proveedor': FProveedor,
		'medida': FMedida,
		'departamento': FDepartamento,
		'ubicacion': FUbicacion,
		'contacto': FContacto
		}
	func=D.get(tipo, lambda: "no existe tipo")
	return func()
#--------------------------------------

#obtener formulario con instance------------------
def FiMarca(qs):
	return MarcaForm(instance=qs)
def FiProducto(qs):
	return ProductoForm(instance=qs)
def FiCliente(qs):
	return ClienteForm(instance=qs)
def FiProveedor(qs):
	return ProveedorForm(instance=qs)
def FiMedida(qs):
	return MedidaForm(instance=qs)
def FiDepartamento(qs):
	return DepartamentoForm(instance=qs)
def FiUbicacion(qs):
	return UbicacionForm(instance=qs)
def FiContacto(qs):
	return ContactoForm(instance=qs)

def get_Fi(tipo,qs):
	D={
		'marca': FiMarca,
		'producto': FiProducto,
		'cliente': FiCliente,
		'proveedor': FiProveedor,
		'medida': FiMedida,
		'departamento': FiDepartamento,
		'ubicacion': FiUbicacion,
		'contacto': FiContacto
		}
	func=D.get(tipo, lambda: "no existe tipo")
	return func(qs)
#---------------------------------------
def productomarca(valor):
	return Productomarcaform(initial=valor)

def productomedida(valor):
	return Productomedidaform(initial=valor)

def productodpto(valor):
	return Productodptoform(initial=valor)

def parcialproducto(tipo,valor):
	D={
		'marca': productomarca,
		'medida': productomedida,
		'departamento': productodpto
	}
	func=D.get(tipo)
	return func(valor)