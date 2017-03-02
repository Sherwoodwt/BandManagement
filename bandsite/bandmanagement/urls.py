from django.conf.urls import url

from bandmanagement.views import (
    list_bands,
    create_band,
    view_band,
    edit_band,
    delete_band,
)

urlpatterns = [
    url(r'^$', list_bands, name='listBands'),
    url(r'^create/$', create_band, name='createBand'),
    url(r'^(?P<band_id>[0-9]+)/$', view_band, name='viewBand'),
    url(r'^(?P<band_id>[0-9]+)/edit/$', edit_band, name='editBand'),
    url(r'^(?P<band_id>[0-9]+)/delete/$', delete_band, name='deleteBand'),
]
