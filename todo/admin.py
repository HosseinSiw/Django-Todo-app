from django.contrib import admin

from todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'is_done')
    list_filter = ('title', 'is_done')
    search_fields = ('title',)


admin.site.register(Todo, TodoAdmin)
