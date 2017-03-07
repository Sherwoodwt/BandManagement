'''views for band management'''
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from bandmanagement.models import Band, Member
from bandmanagement.forms import BandForm, MemberCreateForm

# Create your views here.

# Band Views
@login_required
def list_bands(request):
    '''list of all bands'''
    bands = Band.objects.all()
    context = {
        'band_list': bands
    }
    return render(request, 'band_templates/list_page.html', context)

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
        'form': form,
        'reason': 'Create',
    }
    return render(request, 'band_templates/create.html', context)

@login_required
def edit_band(request, band_id=None):
    '''edit a band model'''
    band = get_object_or_404(Band, pk=band_id)
    if band_id:
        form = BandForm(request.POST or None, instance=band)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('viewBand', kwargs={'band_id': band_id}))
    context = {
        'form': form,
        'reason': 'Edit',
        'band': band,
    }
    return render(request, 'band_templates/create.html', context)

@login_required
def view_band(request, band_id):
    '''view a specific a band model'''
    band = get_object_or_404(Band, pk=band_id)
    members = band.member_set.all()
    is_member = False
    member_id = None

    for member in members:
        if member.user == request.user:
            is_member = True
            member_id = member.pk
            break

    context = {
        'band': band,
        'member_list': members,
        'member_id': member_id,
        'is_member': is_member,
    }
    return render(request, 'band_templates/detail_page.html', context)

@login_required
def delete_band(request, band_id):
    '''delete a band model'''
    band = get_object_or_404(Band, pk=band_id)
    if(band.created_by == request.user):
        band.delete()
    return HttpResponseRedirect(reverse('listBands'))

# Member Views
@login_required
def add_member(request, band_id):
    '''add a new member to the given band. member belongs to current user'''
    band = get_object_or_404(Band, pk=band_id)
    form = MemberCreateForm(request.POST or None, initial={'display_name': request.user.username})
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.band = band
        instance.save()
        return HttpResponseRedirect(reverse('viewBand', kwargs={'band_id': band_id}))
    context = {
        'form': form,
        'band': band,
    }
    return render(request, 'member_templates/create.html', context)

@login_required
def view_member(request, member_id):
    '''view a specific member'''
    member = get_object_or_404(Member, pk=member_id)
    band = member.band
    context = {
        'band': band,
        'member': member,
    }
    return render(request, 'member_templates/detail_page.html', context)

@login_required
def edit_member(request, member_id):
    '''edit a member'''
    return HttpResponse('Not yet available')

@login_required
def delete_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    band = member.band
    if(member.user == request.user):
        member.delete()
        return HttpResponseRedirect(reverse('viewBand', kwargs={'band_id': band.pk}))
    return HttpResponse('You can only delete members that you created!')

