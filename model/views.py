from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from account.models import Profile
from account.views import LoginRequiredMixin
from model.models import ModelR01PG01


class ModelR01PG01CreateView(LoginRequiredMixin, CreateView):
    model = ModelR01PG01
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('model:detail_modelr01pg01', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(ModelR01PG01CreateView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(username=self.request.user.username)
        return context


class ModelR01PG01UpdateView(LoginRequiredMixin, UpdateView):
    model = ModelR01PG01
    fields = '__all__'
    context_object_name = 'model'

    def get_success_url(self):
        return reverse_lazy('model:detail_modelr01pg01', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(ModelR01PG01UpdateView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(username=self.request.user.username)
        return context


class ModelR01PG01DetailView(LoginRequiredMixin, DetailView):
    model = ModelR01PG01
    context_object_name = 'model'

    def get_context_data(self, **kwargs):
        context = super(ModelR01PG01DetailView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(username=self.request.user.username)
        return context


class ModelR01PG01ListView(LoginRequiredMixin, ListView):
    model = ModelR01PG01
    context_object_name = 'model_list'

    def get_context_data(self, **kwargs):
        context = super(ModelR01PG01ListView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(username=self.request.user.username)
        return context


class ModelR01PG01DeleteView(LoginRequiredMixin, DeleteView):
    model = ModelR01PG01
    context_object_name = 'model'
    success_url = reverse_lazy('model:list_modelr01pg01')

    def get_context_data(self, **kwargs):
        context = super(ModelR01PG01DeleteView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(username=self.request.user.username)
        return context
