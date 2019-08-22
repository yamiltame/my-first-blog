
# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from pprint import pprint
import os,sys 
import random 

os.environ['DJANGO_SETTINGS_MODULE'] = 'capacitacion.settings' 
sys.path.append("/opt/capacitacion/") 

from django.core.wsgi import get_wsgi_application 
application = get_wsgi_application() 
from django.test import TestCase

vocales=['a','e','i','o','u']

def ej1(lista):
	suma=0.0
	L=[]
	for e in lista:
		suma=suma+e
		L.append(suma)
	return L

def elimina(lista):
	L=lista
	L.pop(0)
	L.pop(-1)
	return L

def ordenada(lista):
	valor=True
	for i in range(len(lista)-1):
		if(lista[i]>lista[i+1]):
			valor=False
	return valor


def randlist():
	L=[]
	for i in range(23):
		L.append(random.randrange(0,101))
	return L

def quitaduplicado(lista):
	L=list(dict.fromkeys(lista))
	return L

def duplicado(lista):
	newlist=quitaduplicado(lista)
	if (len(newlist)!=len(lista)):
		return True
	else:
		return False

def leertexto(texto):
	file=open(texto,'r')
	Lista=file.read().split(" ")
	return Lista

def inversas(lista):
	L=[]
	for e in lista:
		if e==e[::-1] :
			L.append(e)
	print L

def iniciales(texto):
	words=texto.split(" ")
	ini=""
	for w in words:
		ini=ini+w[0]
	return ini

def contiene(cadena,subcadena):
	return subcadena in cadena

def voc(palabra):
	v=0
	for c in palabra:
		if contiene("aeiouAEIOU",c):
			v+=1
	return v

def vocales(palabra):
	v=[]
	for e in palabra:
		if contiene("aeiouAEIOU",e):
			v.append(e)
	Voc=quitaduplicado(v)
	Voc.sort()
	return Voc

def palabralarga(frase):
	words=frase.split(" ")
	c=0
	big=[""]
	for w in words:
		if(len(w)>len(big[c])):
			big[c]=w
		elif(len(w)==len(big[c])):
			big.append(w)
			c+=1
	return big

def histo(num):
	h=""
	for i in range(num):
		h+="*"
	return h

def contarvocales(texto):
	diccionario={"a":0,"e":0,"i":0,"o":0,"u":0}
	file=open(texto,'r')
	Lista=file.read().split(" ")
	for word in Lista:
		for c in word:
			if contiene("aeiouAEIOU",c):
				l=c.lower()
				diccionario[l]+=1
	for x in diccionario:
		print x,histo(diccionario[x]),"(",diccionario[x],")"

def maketel():
	while True:
		try:
			tel=int(raw_input("ingresa los 10 digitos de tu numero: "))
		except ValueError:
			print "debes ingresar los 10 digitos de tu telefono"
			continue
		if len(str(tel))!=10:
			print "deben ser 10 digitos"
		else:
			break
	fon=str(tel)
	print "Telefono en formato"
	print "(",fon[0:3],")",fon[3:6],"-",fon[6:8],"-",fon[8:10]

def contarpalabras4voc(texto):
	palabras=0
	file=open(texto,'r')
	Lista=file.read().split(" ")
	for word in Lista:
		if(len(vocales(word))>=4):
			palabras+=1
	return palabras


if __name__ == "__main__": 
	print "Ejercicio 1"
	L=[1,2,3]
	print "lista: ",L, " suma: ",ej1(L)
	print "\nEjercicio 2"
	L=[1,2,3,4,5]
	print "lista: ",L," elimina: ",elimina(L)
	L2=["d","a","b","c"]
	print "\nEjercicio3"
	print "lista1: ",L," ordenada: ",ordenada(L)
	print "lista2: ",L2," ordenada: ",ordenada(L2)
	List=randlist()
	print "\nEjercicio4"
	print "generados al azar: \n",List
	print "tiene duplicados: ",duplicado(List)
	print "Ejercicio5"
	print "sin duplicados: \n", quitaduplicado(List)
	print "\nEjercicio6"
	print leertexto("texto.txt")
	P=["oro","animal","radar","pato","rajar"]
	print "\nEjercicio7"
	print "palabras: ", P
	print "inversas: "
	inversas(P)
	print "\nEjercicio8"
	print "hola mundo loco"
	print "iniciales: ", iniciales("hola mundo loco")
	print "\nEjercicio9"
	print "Nacho contiene ac: ", contiene("Nacho","ac")
	print "Aurora contiene sol: ",contiene("Aurora","sol")
	print "\nEjercicio10,11"
	s=raw_input("ingrese su nombre: ")
	print "su nombre tiene ",voc(s)," vocales"
	print "Las cuales son: ",vocales(s)
	print "\nEjercicio12"
	print "pepe pecas pica papas"
	print "palabras largas: ",palabralarga("pepe pecas pica papas")
	print "\nEjercicio13"
	maketel()
	print "\nEjercicio14"
	contarvocales("texto.txt")
	print "\nEjercicio15"
	print "en el texto palabras.txt hay ",contarpalabras4voc("palabras.txt")," palabras con al menos 4 vocales diferentes"