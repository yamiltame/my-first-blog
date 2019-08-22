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

def telegrama(texto,lmax,cpc,cpl):
	dicc={}
	stp=False
	stps=False
	costo=0
	palabra=""
	file=open(texto,'r')
	file2=open("nuevo_texto.txt",'w')
	Lista=file.read().split(" ")
	for word in Lista:
		if(word!=" "):
			if(word[len(word)-1]=="."):
				word=word[0:len(word)-1]
				stp=True
			elif(word[len(word)-2:len(word)]==".\n"):
				stps=True
			else:
				stp=False
				stps=False
			if(word in dicc.keys()):
				palabra=dicc[word]
				costo+=cpl
			elif (len(word)>lmax):
				palabra=word[0:lmax]+"@"
				dicc[word]=palabra
				costo+=cpl
			else:
				palabra=word
				costo+=cpc
		if(stp):
			file2.write(palabra+" STOP ")
		elif(stps):
			file2.write(palabra+" STOPSTOP")
		else:
			file2.write(palabra+" ")
	file.close()
	file2.close()
	print "el costo del telegrama es ",costo," el texto es nuevo_texto.txt"

def monedas():
	dicc={'euro':21.50,'dollar':18.50,'yen':12.56}
	money=raw_input("ingresa una divisa: ")
	if (money.lower() in dicc.keys()):
		print "el valor es de: ",dicc[money.lower()]
	else:
		print "la divisa no esta en el diccionario."

def frutas():
	dicc={'pera':10,'fresa':15,'sandia':18,'limon':14}
	for x in dicc:
		print x," $",dicc[x]
	fruta=raw_input("ingresa una fruta: ")
	if(fruta.lower() in dicc.keys()):
		kilos=int(raw_input("cuantos kilos quieres: "))
		print "el precio de ",kilos," kilos de ",fruta," es ",(kilos*dicc[fruta])
	else:
		print "la fruta que escogiste no esta."

def fecha():
	dicc={'01':'Enero','02':'Febrero','03':'Marzo','04':'Abril','05':'Mayo','06':'Junio','07':'Julio','08':'Agosto','09':'Septiembre','10':'Octubre','11':'Noviembre','12':'Diciembre'}
	fecha=raw_input("ingresa fecha en formato dd/mm/aaaa: ")
	f=fecha.split("/")
	if(len(f)==1):
		print "formato inivalido "
	else:
		if(f[1] in dicc.keys()):
			print f[0]," de ",dicc[f[1]]," de ",f[2]
		else:
			print "no existe el mes"

def curso():
	curso=0
	dicc={'quimica':4,'fisica':4,'matematicas':4}
	for x, v in dicc.items():
		print x," tiene ",v," creditos "
		curso+=v
	print "los creditos del curso son ",curso

def cesta():
	total=0
	dicc={}
	articulo=""
	while(articulo!="0"):
		articulo=raw_input("ingresa nuevo articulo o 0 para terminar: ")
		if(articulo!="0"):
			precio=input("ingresa el precio: ")
			dicc[articulo]=precio
		else:
			print "la cesta es: "
			for x in dicc:
				print x," $",dicc[x]
				total+=dicc[x]
			print "Total: ",total

def traductor():
	special=[".",",","\n"]
	dicc={}
	file=open("words.txt",'r')
	lines=file.readlines()
	for l in lines:
		w=l.split(":")
		if(w[1][len(w[1])-1]=="\n"):
			w[1]=w[1][0:len(w[1])-1]
		dicc[w[0]]=w[1]
	frase=raw_input("ingresa una frase en espagnol: ")
	palabras=frase.split(" ")
	phrase=""
	for p in palabras:
		if(p[len(p)-1] in special):
			real=p[0:len(p)-1]
			s=True
		else:
			real=p
			s=False
		if real in dicc.keys():
			if(s):
				phrase+=dicc[real]+p[len(p)-1]+" "
			else:
				phrase+=dicc[real]+" "

		else:
			phrase+=p+" "
	print phrase
	file.close()

morse={
'a':'.-',
'b':'-...',
'c':'-.-.',
'd':'-..',
'e':'.',
'f':'--.-',
'g':'--.',
'h':'....',
'i':'..',
'j':'.---',
'k':'-.-',
'l':'.-..',
'm':'--',
'n':'-.',
'o':'---',
'p':'.--.',
'q':'--.-',
'r':'.-.',
's':'...',
't':'-',
'u':'..-',
'v':'...-',
'w':'.--',
'x':'-..-',
'y':'-.--',
'z':'--.'
}

def hazmorse(palabra):
	codigo=""
	for w in palabra:
		if w in morse.keys():
			codigo+=morse[w]+" "
		else:
			codigo+=w+" "
	print "La palabra (",palabra,") se escribe: ",codigo[0:len(codigo)-1]," en clave morse"


if __name__ == "__main__": 
	telegrama("texto.txt",5,1,2)
	print "\n"
	monedas()
	print "\n"
	frutas()
	print "\n"
	fecha()
	print "\n"
	curso()
	print "\n"
	cesta()
	print "\n"
	traductor()
	print "\n"
	hazmorse("general")