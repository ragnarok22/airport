from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from account.views import SuperUserRequiredMixin, ProfileMixin
from .models import Training


class TrainingCreateView(SuperUserRequiredMixin, CreateView):
    model = Training


class TrainingUpdateView(SuperUserRequiredMixin, UpdateView):
    model = Training


class TrainingDetailView(ProfileMixin, DetailView):
    model = Training


class TrainingListView(ProfileMixin, ListView):
    model = Training


class TrainingDeleteView(ProfileMixin, DeleteView):
    model = Training
