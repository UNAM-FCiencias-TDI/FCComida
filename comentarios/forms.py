from django import forms
from django.forms import Textarea
from .models import Comentario

class ComercioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		exclude = ('user',)
		fields = ('comentario','comercioId')
		widgets = {
            'comentario': Textarea(attrs={'cols': 30, 'rows': 5}),
        }

