from django.contrib import admin

# Register your models here.
from apps.users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'age', 'phone', 'email')