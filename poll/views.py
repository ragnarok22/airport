from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from account.views import ProfileMixin
from poll.forms import NationalPassengerForm
from poll.models import NationalPassengerPoll, services, Service


class NationalPassengerPollCreateView(ProfileMixin, CreateView):
    model = NationalPassengerPoll
    form_class = NationalPassengerForm
    success_url = reverse_lazy('poll:list_national_passenger')

    def get_context_data(self, **kwargs):
        context = super(NationalPassengerPollCreateView, self).get_context_data(**kwargs)
        context['services'] = services
        return context

    def form_valid(self, form):
        model = form.instance
        model.save()
        iterator = 1
        for s in services:
            service = Service()
            service.title = s
            service.evaluation = self.request.POST['evaluate'+str(iterator)]
            why = self.request.POST.get('why' + str(iterator), None)
            if why:
                service.why = why
            service.national_passenger = form.instance
            service.save()
            iterator += 1
        print(form.instance.pk)
        return super(NationalPassengerPollCreateView, self).form_valid(form)


class NationalPassengerPollListView(ProfileMixin, ListView):
    model = NationalPassengerPoll


class NationalPassengerPollDetailView(ProfileMixin, DetailView):
    model = NationalPassengerPoll


class NationalPassengerPollUpdateView(ProfileMixin, UpdateView):
    model = NationalPassengerPoll
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('poll:detail_national_passenger', kwargs={'pk': self.object.pk})


class NationalPassengerPollDeleteView(ProfileMixin, DeleteView):
    model = NationalPassengerPoll
    success_url = reverse_lazy('poll:list_national_passenger')


class AllPollView(ProfileMixin, TemplateView):
    template_name = 'poll/all_polls.html'
