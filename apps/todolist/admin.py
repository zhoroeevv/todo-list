from django.contrib import admin

# Register your models here.
from apps.todolist.models import ToDo

@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    