from django.conf.urls import url

from taskmanagement.views import (
    create_task,
    list_tasks,
)

urlpatterns = [
    url(r'^$', list_tasks, name='listTasks'),
    url(r'^create/$', create_task, name='createTask'),
]
