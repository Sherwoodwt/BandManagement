from django.conf.urls import url

from bandmanagement.views import (
    list_bands,
    create_band,
    view_band,
)

urlpatterns = [
    url(r'^$', list_bands, name='listBands'),
    url(r'^create/$', create_band, name='createBand'),
    url(r'^(?P<band_id>[0-9]+)/$', view_band, name='viewBand'),
]
