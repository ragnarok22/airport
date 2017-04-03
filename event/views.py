from django.views.generic import CreateView

from account.views import LoginRequiredMixin
from event.models import Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = '__all__'
