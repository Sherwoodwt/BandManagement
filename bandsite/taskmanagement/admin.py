from django.contrib import admin

from taskmanagement.models import (
    Task,
)

# Register your models here.
admin.site.register(Task)
