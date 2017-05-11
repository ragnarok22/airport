from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from account.models import Profile
from account.views import SuperUserRequiredMixin, ProfileMixin
from event.views import EventTodayProfileMixin
from model.forms import EmergencyReportCreateForm
from model.models import ModelR01PG01, Area, LawRequirement, EmergencyReport, RealAnalysis, Analysis


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


class LawRequirementCreateView(SuperUserRequiredMixin, CreateView):
    model = LawRequirement
    fields = ['requirements', 'law', 'section', 'environmental_aspects', 'file']
    template_name = 'law_requirements/lawrequirement_form.html'

    def get_success_url(self):
        return reverse_lazy('model:detail_law', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.register_by = Profile.objects.get(username=self.request.user.username)
        form.instance.save()
        return super(LawRequirementCreateView, self).form_valid(form)


class LawRequirementListView(ProfileMixin, ListView):
    queryset = LawRequirement.objects.all().order_by('pub_date')
    template_name = 'law_requirements/lawrequirement_list.html'
    context_object_name = 'laws'


class LawRequirementDeleteView(SuperUserRequiredMixin, DeleteView):
    model = LawRequirement
    template_name = 'law_requirements/lawrequirement_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('model:list_law')


class LawRequirementDetailView(ProfileMixin, DetailView):
    model = LawRequirement
    template_name = 'law_requirements/lawrequirement_detail.html'


class LawRequirementUpdateView(SuperUserRequiredMixin, UpdateView):
    model = LawRequirement
    fields = ['requirements', 'law', 'section', 'environmental_aspects', 'file']
    template_name = 'law_requirements/lawrequirement_form.html'

    def get_success_url(self):
        return reverse_lazy('model:detail_law', kwargs={'pk': self.object.pk})


class EmergencyReportCreateView(SuperUserRequiredMixin, CreateView):
    form_class = EmergencyReportCreateForm
    template_name = 'emergency/emergencyreport_form.html'


class EmergencyReportUpdateView(SuperUserRequiredMixin, UpdateView):
    model = EmergencyReport
    fields = ['no', 'report', 'datetime', 'place', 'description']
    template_name = 'law_requirements/lawrequirement_form.html'
    context_object_name = 'emergency'

    def get_success_url(self):
        return reverse_lazy('model:detail_emergency', kwargs={'pk': self.object.pk})


class EmergencyReportListView(SuperUserRequiredMixin, ListView):
    model = EmergencyReport
    context_object_name = 'emergency_list'
    template_name = 'emergency/emergencyreport_list.html'


class EmergencyReportDeleteView(SuperUserRequiredMixin, DeleteView):
    model = EmergencyReport
    context_object_name = 'emergency'
    template_name = 'emergency/emergencyreport_confirm_delete.html'


class EmergencyReportDetailView(SuperUserRequiredMixin, DetailView):
    model = EmergencyReport
    context_object_name = 'emergency'
    template_name = 'emergency/emergencyreport_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EmergencyReportDetailView, self).get_context_data(**kwargs)
        context['real_analysiss'] = RealAnalysis.objects.filter(emergency_id=self.object.id)
        return context


class RealAnalysisCreateView(SuperUserRequiredMixin, CreateView):
    model = RealAnalysis
    template_name = 'emergency/real_analysis/realanalysis_form.html'
    fields = ['affections', 'measures', 'first_time', 'cause', 'summary', 'evaluation', 'emergency']

    def form_valid(self, form):
        form.instance.make_by = Profile.objects.get(username=self.request.user.username)
        form.instance.save()
        return super(RealAnalysisCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('model:detail_real_analysis', kwargs={'pk': self.object.pk})


class RealAnalysisUpdateView(SuperUserRequiredMixin, UpdateView):
    model = RealAnalysis
    fields = ['affections', 'measures', 'first_time', 'cause', 'summary', 'evaluation', 'emergency']
    template_name = 'emergency/real_analysis/realanalysis_form.html'

    def get_success_url(self):
        return reverse_lazy('model:detail_real_analysis', kwargs={'pk': self.object.pk})


class RealAnalysisListView(SuperUserRequiredMixin, ListView):
    model = RealAnalysis
    template_name = 'emergency/real_analysis/realanalysis_list.html'


class RealAnalysisDeleteView(SuperUserRequiredMixin, DeleteView):
    model = RealAnalysis
    template_name = 'emergency/real_analysis/realanalysis_confirm_delete.html'
    success_url = reverse_lazy('model:list_real_analysis')


class RealAnalysisDetailView(SuperUserRequiredMixin, DetailView):
    model = RealAnalysis
    template_name = 'emergency/real_analysis/realanalysis_detail.html'
    context_object_name = 'real_analysis'
