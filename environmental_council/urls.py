from django.conf.urls import url

from environmental_council.views import EnvironmentalCouncilCreateView, EnvironmentalCouncilUpdateView, \
    EnvironmentalCouncilDeleteView

urlpatterns = [
    url(r'^create/$', EnvironmentalCouncilCreateView.as_view(), name='create_environmental_council'),
    url(r'^update/(?P<pk>[0-9]+)/$', EnvironmentalCouncilUpdateView.as_view(), name='update_environmental_council'),
    url(r'^delete/(?P<pk>[0-9]+)/$', EnvironmentalCouncilDeleteView.as_view(), name='delete_environmental_council'),
]
