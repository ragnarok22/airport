from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from account.views import ProfileMixin
from poll.models import NationalPassengerPoll


class NationalPassengerPollCreateView(ProfileMixin, CreateView):
    model = NationalPassengerPoll
    fields = '__all__'


class NationalPassengerPollListView(ProfileMixin, ListView):
    model = NationalPassengerPoll


class NationalPassengerPollDetailView(ProfileMixin, DetailView):
    model = NationalPassengerPoll


class NationalPassengerPollUpdateView(ProfileMixin, UpdateView):
    model = NationalPassengerPoll
    fields = '__all__'


class NationalPassengerPollDeleteView(ProfileMixin, DeleteView):
    model = NationalPassengerPoll
