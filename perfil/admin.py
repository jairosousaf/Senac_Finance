from django.contrib import admin

from perfil.models import Categoria, Conta

# Register your models here.

admin.site.register(Conta)
admin.site.register(Categoria)