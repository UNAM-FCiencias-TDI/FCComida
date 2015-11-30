#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    FACULTADES = (
    	('Facultad de Arquitectura', 'Facultad de Arquitectura'),
    	('Facultad de Derecho','Facultad de Derecho'),
    	('Facultad de Ciencias','Facultad de Ciencias'),
    	('Facultad de Ciencias Políticas y Sociales','Facultad de Ciencias Políticas y Sociales'),
    	('Facultad de Contaduría y Administración','Facultad de Contaduría y Administración'),
    	('Facultad de Economía','Facultad de Economía'),
    	('Facultad de Filosofía y Letras','Facultad de Filosofía y Letras'),
    	('Facultad de Ingeniería','Facultad de Ingeniería'),
    	('Facultad de Medicina','Facultad de Medicina'),
    	('Facultad de Química','Facultad de Química'),
    	('Facultad de Odontología','Facultad de Odontología'),
    	('Facultad de Psicología','Facultad de Psicología'),
    	('Facultad de Veterinaria y Zootecnia','Facultad de Veterinaria y Zootecnia'),
    )

    # The additional attributes we wish to include.
    facultad = models.CharField(max_length=200, choices=FACULTADES)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
