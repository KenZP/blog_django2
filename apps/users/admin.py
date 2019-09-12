from django.contrib import admin


# Register your models here.
from .models import UserPro


class UserProAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'gender', "mobile", 'birthday')
    fieldsets = (('用户', {'fields': ('username', 'password',)}),
                      ('个人信息', {'fields': ('name', 'email','gender','mobile','birthday')}),
                      ('权限', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
                      ('其他', {'fields': ('last_login', 'date_joined')}),
                      )


admin.site.register(UserPro, UserProAdmin)
