from django.contrib import admin

from .models import Contato, Desenvolvedor, Habilidade, Projeto

admin.site.register(Contato)
admin.site.register(Desenvolvedor)
admin.site.register(Habilidade)
admin.site.register(Projeto)
