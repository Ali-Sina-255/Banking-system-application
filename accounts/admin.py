from django.contrib import admin
from . models import Account
from django.contrib.auth.admin import UserAdmin
class UserAccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    ordering = ['-date_joined']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Account, UserAccountAdmin)