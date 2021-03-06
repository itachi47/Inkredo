from atexit import unregister
from django.contrib import admin

from api.models import Company, PastEmployee, PresentEmployee, UserHistory
from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm, UserAdminChangeForm

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email', 'admin']
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name', )}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


# Register your models here.
admin.site.register(Company)
admin.site.register(User, UserAdmin)
admin.site.register(UserHistory)
admin.site.register(PresentEmployee)
admin.site.register(PastEmployee)


# Unregister your model here.
admin.site.unregister(Group)
