from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from account.views import SuperUserRequiredMixin, ProfileMixin
from training.forms import TrainingForm
from .models import Training


class TrainingCreateView(SuperUserRequiredMixin, CreateView):
    model = Training
    form_class = TrainingForm
    success_url = reverse_lazy('training:list_training')


class TrainingUpdateView(SuperUserRequiredMixin, UpdateView):
    model = Training
    form_class = TrainingForm
    success_url = reverse_lazy('training:list_training')


class TrainingDetailView(ProfileMixin, DetailView):
    model = Training


class TrainingListView(ProfileMixin, ListView):
    model = Training


class TrainingDeleteView(ProfileMixin, DeleteView):
    model = Training
    success_url = reverse_lazy('training:list_training')
