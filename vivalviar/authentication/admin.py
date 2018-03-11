from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _

from ..authentication.forms import UserChangeForm, UserCreationForm
from ..authentication.models import User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_of_birth', 'is_staff', 'is_superuser')
    list_filter = ('is_staff',)
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     ('Personal info', {'fields': ('date_of_birth',)}),
    #     ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    # )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'date_of_birth')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'date_of_birth', 'password1', 'password2')
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)


admin.site.register(Permission)
