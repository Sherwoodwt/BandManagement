from django.contrib import admin

from bandmanagement.models import (
    Band,
    Member,
)
# Register your models here.
admin.site.register(Band)
admin.site.register(Member)
