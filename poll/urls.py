from django.conf.urls import url

from poll.views import NationalPassengerPollCreateView, NationalPassengerPollListView, \
    NationalPassengerPollUpdateView, NationalPassengerPollDetailView, \
    NationalPassengerPollDeleteView, AllPollView, InternationalPassengerPollCreateView, \
    InternationalPassengerPollListView, InternationalPassengerPollUpdateView, InternationalPassengerPollDetailView, \
    InternationalPassengerPollDeleteView, AirLineRepresentPollCreateView, AirLineRepresentPollListView, \
    AirLineRepresentPollUpdateView, AirLineRepresentPollDetailView, AirLineRepresentPollDeleteView

urlpatterns = [
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

    url(r'airline/represent/create/$', AirLineRepresentPollCreateView.as_view(),
        name='create_airline_represent'),
    url(r'airline/represent/list/$', AirLineRepresentPollListView.as_view(),
        name='list_airline_represent'),
    url(r'airline/represent/update/(?P<pk>[0-9]+)/$', AirLineRepresentPollUpdateView.as_view(),
        name='update_airline_represent'),
    url(r'airline/represent/detail/(?P<pk>[0-9]+)/$', AirLineRepresentPollDetailView.as_view(),
        name='detail_airline_represent'),
    url(r'airline/represent/delete/(?P<pk>[0-9]+)/$', AirLineRepresentPollDeleteView.as_view(),
        name='delete_airline_represent'),

    url(r'all/$', AllPollView.as_view(), name='all_poll'),
]
