from django.contrib import admin
from .models import DayView, Task

class TodoAdmin(admin.ModelAdmin):
    list_display = ('priority','title', 'description', 'completed')


# Register your models here.

admin.site.register(DayView)
admin.site.register(Task, TodoAdmin)