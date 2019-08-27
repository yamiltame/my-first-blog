from django import forms
from .models import Post
from .models import Person

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class PersonForm(forms.ModelForm):
	class Meta:
		model=Person
		#fields=['name','shirt_size','']
		exclude=[]

class user(forms.Form):
	nombre=forms.CharField(label='Nombre',max_length=100)
	fecha_nacimiento=forms.DateField()