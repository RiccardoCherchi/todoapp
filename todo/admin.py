from django.contrib import admin
from .models import Todo

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = ['todo', 'user', 'id']


admin.site.register(Todo, TodoAdmin)
