from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from account.models import Profile
from account.views import ProfileMixin, SuperUserRequiredMixin
from event.views import EventTodayProfileMixin
from model.models import ModelR01PG01, Area


class ModelR01PG01CreateView(EventTodayProfileMixin, CreateView):
    model = ModelR01PG01
    fields = ['year', 'environmental_aspects']

    def get_success_url(self):
        return reverse_lazy('model:detail_modelr01pg01', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.register_by = Profile.objects.get(username=self.request.user.username)
        form.instance.area = Profile.objects.get(username=self.request.user.username).area
        form.instance.save()
        return super(ModelR01PG01CreateView, self).form_valid(form)


class ModelR01PG01UpdateView(EventTodayProfileMixin, UpdateView):
    model = ModelR01PG01
    fields = ['year', 'environmental_aspects']
    context_object_name = 'model'

    def get_success_url(self):
        return reverse_lazy('model:detail_modelr01pg01', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.register_by = Profile.objects.get(username=self.request.user.username)
        form.instance.area = Profile.objects.get(username=self.request.user.username).area
        form.instance.save()
        return super(ModelR01PG01UpdateView, self).form_valid(form)


class ModelR01PG01DetailView(EventTodayProfileMixin, DetailView):
    model = ModelR01PG01
    context_object_name = 'model'

    def get_context_data(self, **kwargs):
        context = super(ModelR01PG01DetailView, self).get_context_data(**kwargs)
        return context


class ModelR01PG01ListView(EventTodayProfileMixin, ListView):
    context_object_name = 'model_list'
    queryset = ModelR01PG01.objects.all().order_by('year').order_by('area__name')


class ModelR01PG01DeleteView(SuperUserRequiredMixin, DeleteView):
    model = ModelR01PG01
    context_object_name = 'model'
    success_url = reverse_lazy('model:list_modelr01pg01')


class AreaCreateView(EventTodayProfileMixin, SuperUserRequiredMixin, CreateView):
    model = Area
    fields = '__all__'
    success_url = reverse_lazy('model:list_area')


class AreaUpdateView(EventTodayProfileMixin, SuperUserRequiredMixin, UpdateView):
    model = Area
    fields = '__all__'


class AreaDetailView(EventTodayProfileMixin, DetailView):
    model = Area

    def get_context_data(self, **kwargs):
        context = super(AreaDetailView, self).get_context_data(**kwargs)
        context['models'] = ModelR01PG01.objects.filter(area__name=self.object.name)
        return context


class AreaListView(EventTodayProfileMixin, ListView):
    model = Area


class AreaDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Area
    success_url = reverse_lazy('model:list_area')
