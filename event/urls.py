from django.conf.urls import url

from event.views import EventCreateView

urlpatterns = [
    url(r'^create/$', EventCreateView.as_view(), name='create_event'),
]
