from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Propaganda,Pyme,Producto,Usuario_Restriccion,Restriccion
# Register your models here.

admin.site.register(Propaganda)
admin.site.register(Pyme)
admin.site.register(Producto)
admin.site.register(Usuario_Restriccion)
admin.site.register(Restriccion)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username','email', 'password1', 'password2')
			}),
		)
