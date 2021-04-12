from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

admin.site.site_header = "INTERNALAYA | Internships and Job Opportunities"

class AccountAdmin(UserAdmin):
	list_display = ('email','firstname','lastname','date_joined', 'last_login', 'is_admin', 'is_staff')
	search_fields = ('email','firstname','lastname')
	readonly_fields=('date_joined', 'last_login')
	ordering = ('email','firstname')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)