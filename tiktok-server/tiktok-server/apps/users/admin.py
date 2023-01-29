from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from apps.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
  list_display = ['email', 'username','first_name','last_name','is_superuser','is_staff','date_joined']

  fieldsets = (
    (None, {'fields': ('username','password')}),
    (_('personal info'), {'fields':( 'first_nam', 'last_name','email')}),
    (_('permissions'), {'fields': ('is_active', 'is_staff','is_superuser','groups','user_permissions'),
    }),
    (_('Important dates'), {'fields': ('last_login','date_joined')}),
  )
  readonly_fields = ['date_joined', 'last_login']

