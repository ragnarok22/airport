from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from account.views import ProfileMixin
from poll.forms import NationalPassengerForm, InternationalPassengerForm
from poll.models import NationalPassengerPoll, services, Service, InternationalPassengerPoll, INTERNATIONAL_SERVICES, \
    InternationalService


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
            service.poll = form.instance
            service.save()
            iterator += 1
        return super(NationalPassengerPollCreateView, self).form_valid(form)


class NationalPassengerPollListView(ProfileMixin, ListView):
    model = NationalPassengerPoll


class NationalPassengerPollDetailView(ProfileMixin, DetailView):
    model = NationalPassengerPoll


class NationalPassengerPollUpdateView(ProfileMixin, UpdateView):
    model = NationalPassengerPoll
    form_class = NationalPassengerForm
    template_name = 'poll/nationalpassengerpoll_update.html'

    def get_success_url(self):
        return reverse_lazy('poll:detail_national_passenger', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        model = form.instance
        model.save()
        iterator = 1
        for s in services:
            service = Service.objects.get(pk=self.request.POST.get('pk' + str(iterator)))
            service.title = s
            service.evaluation = self.request.POST['evaluate' + str(iterator)]
            why = self.request.POST.get('why' + str(iterator), '')
            service.why = why
            service.poll = form.instance
            service.save()
            iterator += 1
        return super(NationalPassengerPollUpdateView, self).form_valid(form)


class NationalPassengerPollDeleteView(ProfileMixin, DeleteView):
    model = NationalPassengerPoll
    success_url = reverse_lazy('poll:list_national_passenger')


class AllPollView(ProfileMixin, TemplateView):
    template_name = 'poll/all_polls.html'


class InternationalPassengerPollCreateView(ProfileMixin, CreateView):
    model = InternationalPassengerPoll
    form_class = InternationalPassengerForm

    def get_success_url(self):
        return reverse_lazy('poll:detail_international_passenger', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(InternationalPassengerPollCreateView, self).get_context_data(**kwargs)
        context['services'] = INTERNATIONAL_SERVICES
        return context

    def form_valid(self, form):
        model = form.instance
        model.save()
        iterator = 1
        for s in INTERNATIONAL_SERVICES:
            service = InternationalService()
            service.title = s
            service.evaluation = self.request.POST['evaluate'+str(iterator)]
            why = self.request.POST.get('why' + str(iterator), None)
            if why:
                service.why = why
            service.poll = form.instance
            service.save()
            iterator += 1
        return super(InternationalPassengerPollCreateView, self).form_valid(form)


class InternationalPassengerPollUpdateView(ProfileMixin, UpdateView):
    model = InternationalPassengerPoll
    form_class = InternationalPassengerForm
    template_name = 'poll/internationalpassengerpoll_update.html'

    def form_valid(self, form):
        model = form.instance
        model.save()
        iterator = 1
        for s in INTERNATIONAL_SERVICES:
            service = InternationalService.objects.get(pk=self.request.POST.get('pk' + str(iterator)))
            service.title = s
            service.evaluation = self.request.POST['evaluate' + str(iterator)]
            why = self.request.POST.get('why' + str(iterator), '')
            service.why = why
            service.poll = form.instance
            service.save()
            iterator += 1
        return super(InternationalPassengerPollUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('poll:detail_international_passenger', kwargs={'pk': self.object.pk})


class InternationalPassengerPollListView(ProfileMixin, ListView):
    model = InternationalPassengerPoll


class InternationalPassengerPollDetailView(ProfileMixin, DetailView):
    model = InternationalPassengerPoll


class InternationalPassengerPollDeleteView(ProfileMixin, DeleteView):
    model = InternationalPassengerPoll
    success_url = reverse_lazy('poll:list_international_passenger')
