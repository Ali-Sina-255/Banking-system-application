from django.contrib import admin
from .models import Account, UserAccount, KYCModel
from django.contrib.auth.admin import UserAdmin


class KYCAdmin(admin.ModelAdmin):
    list_editable = ['account_status', 'account_balance']
    list_display = ['user', 'account_number', 'account_status', 'account_balance']
    list_filter = ['account_status']


admin.site.register(UserAccount, KYCAdmin)


class UserAccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    ordering = ['-date_joined']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, UserAccountAdmin)


class KYCModelAdmin(admin.ModelAdmin):
    list_display = ['full_name','marrital_status','gender']
    list_filter = ['gender','identity_id']


admin.site.register(KYCModel,KYCModelAdmin,)