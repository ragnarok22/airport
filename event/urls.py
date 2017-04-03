from django.conf.urls import url

from event.views import EventCreateView, EventListView, EventTodayListView, EventDetailView, EventDeleteView

urlpatterns = [
    url(r'^create/$', EventCreateView.as_view(), name='create_event'),
    url(r'^list/$', EventListView.as_view(), name='list_event'),
    url(r'^list/today/$', EventTodayListView.as_view(), name='list_event_today'),
    url(r'^detail/(?P<pk>[0-9]+)/$', EventDetailView.as_view(), name='detail_event'),
    url(r'^delete/(?P<pk>[0-9]+)/$', EventDeleteView.as_view(), name='delete_event'),
]
