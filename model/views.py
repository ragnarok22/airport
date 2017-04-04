from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from account.views import LoginRequiredMixin, ProfileMixin
from event.views import EventTodayMixin
from model.models import ModelR01PG01


class ModelR01PG01CreateView(LoginRequiredMixin, EventTodayMixin, ProfileMixin, CreateView):
    model = ModelR01PG01
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('model:detail_modelr01pg01', kwargs={'pk': self.object.pk})


class ModelR01PG01UpdateView(LoginRequiredMixin, EventTodayMixin, ProfileMixin, UpdateView):
    model = ModelR01PG01
    fields = '__all__'
    context_object_name = 'model'

    def get_success_url(self):
        return reverse_lazy('model:detail_modelr01pg01', kwargs={'pk': self.object.pk})


class ModelR01PG01DetailView(LoginRequiredMixin, EventTodayMixin, ProfileMixin, DetailView):
    model = ModelR01PG01
    context_object_name = 'model'

    def get_context_data(self, **kwargs):
        context = super(ModelR01PG01DetailView, self).get_context_data(**kwargs)
        return context


class ModelR01PG01ListView(LoginRequiredMixin, EventTodayMixin, ProfileMixin, ListView):
    model = ModelR01PG01
    context_object_name = 'model_list'


class ModelR01PG01DeleteView(LoginRequiredMixin, ProfileMixin, DeleteView):
    model = ModelR01PG01
    context_object_name = 'model'
    success_url = reverse_lazy('model:list_modelr01pg01')
