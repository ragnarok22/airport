from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from account.views import SuperUserRequiredMixin
from environmental_council.models import EnvironmentalCouncil


class EnvironmentalCouncilCreateView(SuperUserRequiredMixin, CreateView):
    model = EnvironmentalCouncil
    fields = '__all__'
    template_name = 'environmental_council/environmentalcouncil_form.html'
    success_url = reverse_lazy('dashboard')


class EnvironmentalCouncilUpdateView(SuperUserRequiredMixin, UpdateView):
    model = EnvironmentalCouncil
    fields = '__all__'
    success_url = reverse_lazy('dashboard')


class EnvironmentalCouncilDeleteView(SuperUserRequiredMixin, DeleteView):
    model = EnvironmentalCouncil
    success_url = reverse_lazy('dashboard')
