from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ('email', 'firstname', 'lastname', 'is_verified', 'is_active', 'is_superuser', 'created_at')
   
    readonly_fields = ('uuid',)
    list_display = ('uuid', 'email', 'firstname')


admin.site.register(User, UserAdmin)

