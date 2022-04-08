from django.contrib import admin
from .models import Todo
#给数据库增加新的table

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)