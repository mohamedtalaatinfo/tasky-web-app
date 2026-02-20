from django.contrib import admin
from .models import TaskyModel, ComplishedTaskModel
# Register your models here.


class TaskyModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'priority', 'complished']
    list_filter = ['date', 'priority', 'complished']


class ComplishedTaskModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'priority']
    list_filter = ['date', 'priority']



admin.site.register(TaskyModel, TaskyModelAdmin)
admin.site.register(ComplishedTaskModel, ComplishedTaskModelAdmin)