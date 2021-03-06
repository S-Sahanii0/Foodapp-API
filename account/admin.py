from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

admin.site.site_header = "Foodapp API"

class AccountAdmin(UserAdmin):
	list_display = ('email','fullname','date_joined', 'last_login', 'is_admin', 'is_staff')
	search_fields = ('email','fullname')
	readonly_fields=('date_joined', 'last_login')
	ordering = ('email','fullname')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)