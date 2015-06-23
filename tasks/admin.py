from django.contrib import admin

from .models import CurrentTask, TaskType

class TaskAdmin(admin.ModelAdmin):
    search_fields = ['task']
    list_filter = ['task']
    list_display = ('task', 'frequency', 'description')

class TaskAdmin2(admin.ModelAdmin):
    search_fields = ['task']
    list_filter = ['type']
    list_display = ('type', 'person_in_charge', 'date_due')

admin.site.register(CurrentTask, TaskAdmin)
admin.site.register(TaskType, TaskAdmin2)