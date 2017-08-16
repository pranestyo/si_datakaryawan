from django.contrib import admin

from dinas.models import AkunDinas
# Register your models here.

class AkunDinasAdmin(admin.ModelAdmin):
	list_display = ['akun','kabupatenkota']
	list_filter = ()
	search_fields = []
	list_per_page = 25

admin.site.register(AkunDinas, AkunDinasAdmin)