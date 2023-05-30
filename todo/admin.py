from django.contrib import admin

from .models import Task, Tag 


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'due_date', 'status')
    list_filter = ('status', 'tags')
    search_fields = ('title',)
    fieldsets = (
        (None, {'fields': ('title', 'description')}),
        ('Date Information', {'fields': ('due_date',)}),
        ('Status', {'fields': ('status',)}),
        ('Tags', {'fields': ('tags',)})
    )

admin.site.register(Task, TaskAdmin)
admin.site.register(Tag)

