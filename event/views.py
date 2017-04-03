from django.db.models import Q
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from account.views import LoginRequiredMixin
from event.models import Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = '__all__'


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'events_list'

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['event_list'] = self.model.objects.filter(Q(date__day=timezone.now().day)
                                                                 & Q(date__month=timezone.now().month))
        return context


class EventTodayListView(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'event_list'

    def get_queryset(self):
        return self.model.objects.filter(Q(date__day=timezone.now().day) & Q(date__month=timezone.now().month))


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['event_list'] = self.model.objects.filter(Q(date__day=timezone.now().day) &
                                                          Q(date__month=timezone.now().month))
        return context


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('event:detail_event', kwargs={'pk': self.object.pk})


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('event:list_event')
