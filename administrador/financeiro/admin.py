from django.contrib import admin

from .models import Finance
from .models import Receita
from .models import Empresa


class FinanceAdmin(admin.ModelAdmin):

    list_display = ['name', 'loja', 'start_date', 'created_at']
    search_fields = ['name', 'loja']
    prepopulated_fields = {'loja': ('name',)}


admin.site.register(Finance, FinanceAdmin)


class ReceitaAdmin(admin.ModelAdmin):

    list_display = ['name', 'origem', 'start_date', 'created_at']
    search_fields = ['name', 'origem']
    prepopulated_fields = {'origem': ('name',)}

admin.site.register(Receita, ReceitaAdmin)


class EmpresaAdmin(admin.ModelAdmin):

    list_display = ['name', 'origem', 'cnpj' ,'endereco' , 'email' , 'origem', 'start_date', 'created_at']
    search_fields = ['name', 'email']
    prepopulated_fields = {'email': ('name',)}

admin.site.register(Empresa, EmpresaAdmin)




