from django import forms

class FormVHS(forms.Form):
    titulo = forms.CharField()
    genero = forms.CharField()
    anioLanzamiento = forms.IntegerField()
    director = forms.CharField()

class FormCds(forms.Form):
    nombre = forms.CharField()
    artista = forms.CharField()
    anioLanzamiento = forms.IntegerField()
    genero = forms.CharField()

class FormJuegos(forms.Form):
    nombre = forms.CharField()
    desarrolladora = forms.CharField()
    plataforma = forms.CharField()
    genero = forms.CharField()