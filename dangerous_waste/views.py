from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from account.models import Profile
from account.views import SuperUserRequiredMixin, ProfileMixin
from dangerous_waste.models import DangerousWaste


class DangerousWasteCreateView(ProfileMixin, CreateView):
    model = DangerousWaste
    fields = ['airport']
    success_url = reverse_lazy('waste:list_dangerous_waste')

    def form_valid(self, form):
        form.instance.made_by = Profile.objects.get(username=self.request.user.username)
        form.instance.save()
        return super(DangerousWasteCreateView, self).form_valid(form)


class DangerousWasteDeleteView(SuperUserRequiredMixin, DeleteView):
    model = DangerousWaste


class DangerousWasteListView(ProfileMixin, ListView):
    model = DangerousWaste


class DangerousWasteDetailView(ProfileMixin, DetailView):
    model = DangerousWaste


class DangerousWasteUpdateView(ProfileMixin, UpdateView):
    model = DangerousWaste
    fields = ['airport']

    def get_success_url(self):
        return reverse_lazy('waste:detail_dangerous_waste', kwargs={'pk': self.object.pk})
