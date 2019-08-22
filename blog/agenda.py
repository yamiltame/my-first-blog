from __future__ import unicode_literals

from pprint import pprint
import os,sys 
import random 

os.environ['DJANGO_SETTINGS_MODULE'] = 'capacitacion.settings' 
sys.path.append("/opt/capacitacion/") 

from django.core.wsgi import get_wsgi_application 
application = get_wsgi_application() 
from django.test import TestCase

agenda={}
count=0;

def getname():
	nombre=raw_input("ingresa el nombre: ")
	return nombre

def gettel(n):
	while True:
		try:
			tel=int(raw_input(str(n)+": "))
		except ValueError:
			print "deben ser digitos"
			continue
		if (len(str(tel))!=10 and tel!=0):
			print "deben ser 10 digitos"
		else:
			break
	return str(tel)

def maketel(tel):
	return "(",fon[0:3],")",fon[3:6],"-",fon[6:8],"-",fon[8:10]

def getstring(n):
	dato=raw_input(str(n)+": ")
	return dato

def getinfo(dato,captura):
	n=1
	lista=[]
	print "ingresa ",dato,"(s) o 0 para terminar"
	param=captura(n)
	while(param!="0"):
		lista.append(param)
		n+=1
		param=captura(n)
	return lista


def getcontacto(datos):
	switch={'telefono':gettel}
	contacto={}
	for d in datos:
		captura=switch.get(d,lambda n: getstring(n))
		contacto[d]=getinfo(d,captura)
	return contacto

def gethobbies(hobbies):
	pasatiempos={}
	for h in hobbies:
		pasatiempos[h]=getinfo(h,getstring)
	return pasatiempos

def agregar(clave):
	if not clave in agenda.keys():
		nombre=getname()
		contacto=getcontacto(['telefono','email'])
		hobbies=gethobbies(['deportes','musica','peliculas'])
		agenda[clave]={'nombre':nombre,'contacto':contacto,'pasatiempos':hobbies}
	else:
		print "el usuario con esa clave ya existe"




def editar(clave):
	funciones={
		'nombre':getname,
		'contacto'
	}
	if clave in agenda.keys():
		user=agenda.get(clave)
		print "Si deseas editar el campo ingresa 1, si no 0"
		for x,v in user:
			print x," valor actual: ",v
			if(editar()):

		#agregar
	else:
		print "el usuario con esa clave no existe"

def eliminar(clave):
	if clave in agenda.keys():
		user=agenda.get(clave)
		print "ELIMINAR CONTACTO: ",user['nombre'],"\n"
		del agenda[clave]
	else:
		print "el usuario con esa clave no existe"

def veragenda(clave=None):
	pprint(agenda)

def menu():
	global count
	print "ESCOGE UNA OPCION"
	opcion=10
	while True:
		try:
			opcion=int(raw_input("1.Agregar contacto\t 2.Editar contacto\t 3.Eliminar contacto\t 4.Ver agenda\t 0.Salir\n"))
		except ValueError:
			print "opcion invalida"
			continue
		if opcion not in (0,1,2,3,4):
			print "opcion invalida"
		else:
			break
	if(opcion==0):
		sys.exit("adios")
	if(opcion==1):
		clave="auto"+str(count)
		count+=1
	if(opcion!=4 and opcion!=1):
		clave=raw_input("ingresa la clave del contacto: ")
	if(opcion==4):
		clave=""
	dicc={1: agregar, 2: editar, 3: eliminar, 4: veragenda}
	func=dicc.get(opcion)
	func(clave)

if __name__ == "__main__":
	while True:
		menu()