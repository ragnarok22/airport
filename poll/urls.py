from django.conf.urls import url

from poll.views import NationalPassengerPollCreateView, NationalPassengerPollListView, \
    NationalPassengerPollUpdateView, NationalPassengerPollDetailView, \
    NationalPassengerPollDeleteView, AllPollView

urlpatterns = [
    url(r'national/passenger/create/$', NationalPassengerPollCreateView.as_view(),
        name='create_national_passenger'),
    url(r'national/passenger/list/$', NationalPassengerPollListView.as_view(),
        name='list_national_passenger'),
    url(r'national/passenger/update/(?P<pk>[0-9]+)/$', NationalPassengerPollUpdateView.as_view(),
        name='update_national_passenger'),
    url(r'national/passenger/detail/(?P<pk>[0-9]+)/$', NationalPassengerPollDetailView.as_view(),
        name='detail_national_passenger'),
    url(r'national/passenger/delete/(?P<pk>[0-9]+)/$', NationalPassengerPollDeleteView.as_view(),
        name='delete_national_passenger'),

    url(r'all/$', AllPollView.as_view(), name='all_poll'),
]
