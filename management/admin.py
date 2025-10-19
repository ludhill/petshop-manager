from django.contrib import admin
from .models import TipoAnimal, Raca, Animal # 1. Importe seus modelos

# 2. Registre cada modelo para que apareçam no admin
admin.site.register(TipoAnimal)
admin.site.register(Raca)
admin.site.register(Animal)