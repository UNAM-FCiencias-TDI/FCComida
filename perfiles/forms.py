from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password','password2')

    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username

    def clean_email(self):
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Correo ya registrado')
        return email

    def clean_password(self):
        if not self.cleaned_data['password']:
            raise forms.ValidationError("Introduce una contrasena")
        return self.cleaned_data['password']

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contrasenas no coinciden.')
        return password2


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('facultad', 'picture')

"""
class RecuperaPasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
"""