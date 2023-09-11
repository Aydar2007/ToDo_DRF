from django.contrib import admin
from apps.todo.models import ToDo

@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list = ('user', 'title', 'description', 'completed')