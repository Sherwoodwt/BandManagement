'''views for band management'''
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse

# Create your views here.
def initialView(request):
    '''will kill this eventually'''
    return HttpResponse('I am alive')

def create_band(request):
    '''create a band model'''
    return HttpResponse('I am alive')

def edit_band(request):
    '''create a band model'''
    return HttpResponse('I am alive')

def view_band(request):
    '''create a band model'''
    return HttpResponse('I am alive')

def delete_band(request):
    '''create a band model'''
    return HttpResponse('I am alive')
