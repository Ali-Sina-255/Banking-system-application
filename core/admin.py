from django.contrib import admin
from core.models import UserAccount, KYC


class KycAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name']
    list_filter = ['full_name']



class UserAccountAdmin(admin.ModelAdmin):
    list_editable = ['account_status', 'account_balance']
    list_display = ['user', 'account_status', 'account_number', 'account_balance']
    list_filter = ['account_status']


admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(KYC,KycAdmin)