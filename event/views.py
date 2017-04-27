from django.db.models import Q
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from account.views import ProfileMixin
from event.models import Event


class EventTodayMixin(object):
    def get_context_data(self, **kwargs):
        context = super(EventTodayMixin, self).get_context_data(**kwargs)
        context['event_today_list'] = Event.objects.filter(
            Q(date__day=timezone.now().day) & Q(date__month=timezone.now().month))[:5]
        return context


class EventTodayProfileMixin(EventTodayMixin, ProfileMixin):
    pass


class EventCreateView(EventTodayProfileMixin, CreateView):
    model = Event
    fields = '__all__'
    success_url = reverse_lazy('event:list_event')


class EventListView(EventTodayProfileMixin, ListView):
    model = Event
    context_object_name = 'events_list'


class EventTodayListView(EventTodayProfileMixin, ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'event/event_list_today.html'
    queryset = Event.objects.filter(
        Q(date__day=timezone.now().day) & Q(date__month=timezone.now().month))


class EventDetailView(EventTodayProfileMixin, DetailView):
    model = Event


class EventUpdateView(EventTodayProfileMixin, UpdateView):
    model = Event
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('event:detail_event', kwargs={'pk': self.object.pk})


class EventDeleteView(ProfileMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('event:list_event')
