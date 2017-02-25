'''views for band management'''
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from bandmanagement.models import Band
from bandmanagement.forms import BandForm

# Create your views here.
@login_required
def list_bands(request):
    '''will kill this eventually'''
    bands = Band.objects.all()
    context = {
        'band_list': bands
    }
    return render(request, 'list_page.html', context)

@login_required
def create_band(request):
    '''create a band model'''
    form = BandForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        return HttpResponseRedirect(reverse('listBands'))
    context = {
        'form': form
    }
    return render(request, 'create.html', context)

@login_required
def edit_band(request):
    '''edit a band model'''
    return HttpResponse('I am alive')

@login_required
def view_band(request, band_id):
    '''view a specific a band model'''
    band = get_object_or_404(Band, pk=band_id)
    members = band.member_set.all()
    context = {
        'band': band,
        'member_list': members,
    }
    return render(request, 'detail_page.html', context)

@login_required
def delete_band(request, band_id):
    '''delete a band model'''
    band = get_object_or_404(Band, pk=band_id)
    band.delete()
    return HttpResponseRedirect(reverse('listBands'))
