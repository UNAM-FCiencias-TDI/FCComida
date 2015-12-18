from django import forms
from django.forms import Textarea
from .models import Comercio

class ComercioForm(forms.ModelForm):
	class Meta:
		model = Comercio
		fields = ('clave','comedor','facultad','nombre',
			'foto','mayor_precio','menor_precio','descripcion','latitud','longitud')
		widgets = {
            'descripcion': Textarea(attrs={'cols': 30, 'rows': 5}),
        }
