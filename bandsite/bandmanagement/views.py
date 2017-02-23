'''views for band management'''
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse

# Create your views here.
def initialView(request):
    '''will kill this eventually'''
    return HttpResponse('I am alive')
