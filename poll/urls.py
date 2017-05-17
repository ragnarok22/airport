from django.conf.urls import url

from poll.views import NationalPassengerPollCreateView, NationalPassengerPollListView, \
    NationalPassengerPollUpdateView, NationalPassengerPollDetailView, \
    NationalPassengerPollDeleteView, AllPollView, InternationalPassengerPollCreateView, \
    InternationalPassengerPollListView, InternationalPassengerPollUpdateView, InternationalPassengerPollDetailView, \
    InternationalPassengerPollDeleteView

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

    url(r'international/passenger/create/$', InternationalPassengerPollCreateView.as_view(),
        name='create_international_passenger'),
    url(r'international/passenger/list/$', InternationalPassengerPollListView.as_view(),
        name='list_international_passenger'),
    url(r'international/passenger/update/(?P<pk>[0-9]+)/$', InternationalPassengerPollUpdateView.as_view(),
        name='update_international_passenger'),
    url(r'international/passenger/detail/(?P<pk>[0-9]+)/$', InternationalPassengerPollDetailView.as_view(),
        name='detail_international_passenger'),
    url(r'international/passenger/delete/(?P<pk>[0-9]+)/$', InternationalPassengerPollDeleteView.as_view(),
        name='delete_international_passenger'),

    url(r'all/$', AllPollView.as_view(), name='all_poll'),
]
