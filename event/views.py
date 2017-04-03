from django.db.models import Q
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, DetailView, DeleteView

from account.views import LoginRequiredMixin
from event.models import Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = '__all__'


class EventListView(LoginRequiredMixin, ListView):
    model = Event


class EventTodayListView(LoginRequiredMixin, ListView):
    model = Event

    def get_queryset(self):
        return self.model.objects.filter(Q(date__day=timezone.now().day) & Q(date__month=timezone.now().month))


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('event:list_event')
