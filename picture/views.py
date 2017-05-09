from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from django.views.generic import TemplateView

from account.models import Profile
from account.views import ProfileMixin
from picture.models import Image


class PictureListView(ProfileMixin, ListView):
    model = Image


class PictureCreateView(ProfileMixin, CreateView):
    model = Image
    fields = ['image', 'description']
    success_url = reverse_lazy('picture:list_picture')

    def form_valid(self, form):
        form.instance.up_by = Profile.objects.get(username=self.request.user.username)
        form.instance.save()
        return super(PictureCreateView, self).form_valid(form)


class PictureDeleteView(ProfileMixin, DeleteView):
    model = Image
    success_url = reverse_lazy('picture:list_picture')


class PresentationView(TemplateView):
    template_name = 'picture/presentation.html'

    def get_context_data(self, **kwargs):
        context = super(PresentationView, self).get_context_data(**kwargs)
        context['picture_list'] = Image.objects.all()
        return context
