from django.contrib import admin

# Register your models here.
from . models import Compra, Usuario

admin.site.register(Compra)
admin.site.register(Usuario)