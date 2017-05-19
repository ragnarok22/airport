from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from account.views import SuperUserRequiredMixin, ProfileMixin
from bulletin.forms import BulletinForm
from bulletin.models import Bulletin


class BulletinCreateView(SuperUserRequiredMixin, CreateView):
    model = Bulletin
    form_class = BulletinForm

    def get_success_url(self):
        return reverse_lazy('bulletin:list_bulletin')


class BulletinUpdateView(SuperUserRequiredMixin, UpdateView):
    model = Bulletin
    form_class = BulletinForm

    def get_success_url(self):
        return reverse_lazy('bulletin:list_bulletin')


class BulletinListView(ProfileMixin, ListView):
    model = Bulletin
    queryset = Bulletin.objects.all().order_by('-pub_date')


class BulletinDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Bulletin
    success_url = reverse_lazy('bulletin:list_bulletin')
