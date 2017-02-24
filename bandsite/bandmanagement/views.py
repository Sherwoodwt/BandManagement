'''views for band management'''
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect, HttpResponse

from bandmanagement.models import Band
from bandmanagement.forms import BandForm

# Create your views here.
def list_bands(request):
    '''will kill this eventually'''
    bands = Band.objects.all()
    context = {
        'band_list': bands
    }
    return render(request, 'list_page.html', context)

def create_band(request):
    '''create a band model'''
    form = BandForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
    context = {
        'form': form
    }
    return render(request, 'create.html', context)

def edit_band(request):
    '''create a band model'''
    return HttpResponse('I am alive')

def view_band(request, band_id):
    '''create a band model'''
    band = get_object_or_404(Band, pk=band_id)
    members = band.member_set.all()
    context = {
        'band': band,
        'member_list': members,
    }
    return render(request, 'detail_page.html', context)

def delete_band(request):
    '''create a band model'''
    return HttpResponse('I am alive')
