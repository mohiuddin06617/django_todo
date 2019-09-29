from django.contrib import admin
from .models import TodoList, Category


# Register your models here.

class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'due_date', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Category, CategoryAdmin)
