from django.conf.urls import url, include

from bandmanagement.views import (
    home,
    list_all_bands,
    create_band,
    view_band,
    edit_band,
    delete_band,
    add_member,
    view_member,
    edit_member,
    delete_member,
)

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^bands/$', list_all_bands, name='listAllBands'),
    url(r'^create/$', create_band, name='createBand'),
    url(r'^(?P<band_id>[0-9]+)/$', view_band, name='viewBand'),
    url(r'^(?P<band_id>[0-9]+)/edit/$', edit_band, name='editBand'),
    url(r'^(?P<band_id>[0-9]+)/delete/$', delete_band, name='deleteBand'),
    url(r'^(?P<band_id>[0-9]+)/addmember/$', add_member, name='addMember'),
    url(r'^member/(?P<member_id>[0-9]+)/$', view_member, name='viewMember'),
    url(r'^member/(?P<member_id>[0-9]+)/edit/$', edit_member, name='editMember'),
    url(r'^member/(?P<member_id>[0-9]+)/delete/$', delete_member, name='deleteMember'),
    url(r'^(?P<band_id>[0-9]+)/task/', include('taskmanagement.urls')),
]
