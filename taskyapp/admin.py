from django.contrib import admin
from .models import TaskyModel
# Register your models here.


class TaskyModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'priority', 'complished']
    list_filter = ['date', 'priority', 'complished']



admin.site.register(TaskyModel, TaskyModelAdmin)
