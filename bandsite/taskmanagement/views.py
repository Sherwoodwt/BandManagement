from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Task Management
from taskmanagement.forms import TaskForm
from taskmanagement.models import Task

# Band Management
from bandmanagement.models import Band, Member

# Create your views here.

# Task views
@login_required
def create_task(request, band_id):
    '''create a new task'''
    form = TaskForm(request.POST or None)
    band = get_object_or_404(Band, pk=band_id)
    member_list = band.member_set.all()
    form.fields['assignee'].queryset = member_list
    if form.is_valid():
        instance = form.save(commit=False)
        instance.band = band
        instance.save()
        return HttpResponseRedirect(reverse('listTasks', kwargs={'band_id':band.id}))
    context = {
        'form': form,
        'band': band,
        'members': member_list,
    }
    return render(request, 'task_templates/create.html', context)

@login_required
def list_tasks(request, band_id):
    '''list all of a bands tasks'''
    band = get_object_or_404(Band, pk=band_id)
    current_member = get_object_or_404(Member, user=request.user, band=band)
    task_list = band.task_set.all()
    context = {
        'band': band,
        'member': current_member,
        'tasks': task_list,
    }
    return render(request, 'task_templates/list_page.html', context)
