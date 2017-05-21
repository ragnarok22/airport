from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.views.generic import FormView

from account.models import Profile
from account.views import SuperUserRequiredMixin, ProfileMixin
from training.forms import TrainingForm, RegisterForm
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


class TrainingListView(ProfileMixin, FormView):
    template_name = 'training/training_list.html'
    success_url = reverse_lazy('training:list_training')
    form_class = RegisterForm

    def get_context_data(self, **kwargs):
        context = super(TrainingListView, self).get_context_data(**kwargs)
        context['training_list'] = Training.objects.all()
        return context

    def form_valid(self, form):
        id_training = form.cleaned_data.get('training')
        register = form.cleaned_data.get('register', 'None')
        profile = Profile.objects.get(username=self.request.user.username)
        training = None
        if id_training:
            training = Training.objects.get(pk=id_training)
        if register and id_training:
            training.register.add(profile)
        elif register != 'None' and training:
            training.register.remove(profile)
        return super(TrainingListView, self).form_valid(form)


class TrainingDeleteView(ProfileMixin, DeleteView):
    model = Training
    success_url = reverse_lazy('training:list_training')
