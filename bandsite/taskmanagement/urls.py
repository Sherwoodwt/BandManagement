from django.conf.urls import url

from taskmanagement.views import (
    create_task,
)

urlpatterns = [
    url(r'^create/$', create_task, name='createTask'),
]
