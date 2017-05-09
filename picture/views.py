from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView

from account.models import Profile
from account.views import ProfileMixin, LoginRequiredMixin
from picture.models import Image


class PictureListView(ProfileMixin, ListView):
    model = Image


class PictureCreateView(ProfileMixin, CreateView):
    model = Image
    fields = ['image']
    success_url = reverse_lazy('picture:list_picture')

    def form_valid(self, form):
        form.instance.up_by = Profile.objects.get(username=self.request.user.username)
        form.instance.save()
        return super(PictureCreateView, self).form_valid(form)


class PictureDeleteView(ProfileMixin, DeleteView):
    model = Image
    success_url = reverse_lazy('picture:list_picture')
