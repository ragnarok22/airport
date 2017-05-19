from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.views.generic import TemplateView

from account.models import Profile
from account.views import SuperUserRequiredMixin, ProfileMixin
from event.views import EventTodayProfileMixin
from model.forms import EmergencyReportCreateForm, SimulationAnalysisCreateForm, CommunicationForm
from model.models import ModelR01PG01, Area, LawRequirement, EmergencyReport, RealAnalysis, SimulationAnalysis, \
    Communication


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


class ModelR01PG01ListView(EventTodayProfileMixin, TemplateView):
    template_name = 'model/modelr01pg01_list.html'

    def get_context_data(self, **kwargs):
        context = super(ModelR01PG01ListView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(username=self.request.user.username)
        area = Area.objects.get(pk=profile.area.pk)
        context['area'] = area
        context['models'] = ModelR01PG01.objects.filter(area__name=area.name)
        return context


class ModelR01PG01ListAllView(EventTodayProfileMixin, ListView):
    context_object_name = 'model_list'
    queryset = ModelR01PG01.objects.all().order_by('year').order_by('area__name')
    template_name = 'model/modelr01pg01_list_all.html'


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


class EmergencyReportCreateView(EventTodayProfileMixin, CreateView):
    form_class = EmergencyReportCreateForm
    template_name = 'emergency/emergencyreport_form.html'
    success_url = reverse_lazy('model:list_emergency')


class EmergencyReportUpdateView(EventTodayProfileMixin, UpdateView):
    model = EmergencyReport
    fields = ['no', 'report', 'datetime', 'place', 'description']
    template_name = 'law_requirements/lawrequirement_form.html'
    context_object_name = 'emergency'

    def get_success_url(self):
        return reverse_lazy('model:detail_emergency', kwargs={'pk': self.object.pk})


class EmergencyReportListView(EventTodayProfileMixin, ListView):
    model = EmergencyReport
    context_object_name = 'emergency_list'
    template_name = 'emergency/emergencyreport_list.html'


class EmergencyReportDeleteView(SuperUserRequiredMixin, DeleteView):
    model = EmergencyReport
    context_object_name = 'emergency'
    template_name = 'emergency/emergencyreport_confirm_delete.html'


class EmergencyReportDetailView(EventTodayProfileMixin, DetailView):
    model = EmergencyReport
    context_object_name = 'emergency'
    template_name = 'emergency/emergencyreport_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EmergencyReportDetailView, self).get_context_data(**kwargs)
        context['real_analysiss'] = RealAnalysis.objects.filter(emergency_id=self.object.id)
        context['simulation_analysiss'] = SimulationAnalysis.objects.filter(emergency_id=self.object.id)
        return context


class RealAnalysisCreateView(EventTodayProfileMixin, CreateView):
    model = RealAnalysis
    template_name = 'emergency/real_analysis/realanalysis_form.html'
    fields = ['affections', 'measures', 'first_time', 'cause', 'summary', 'evaluation', 'emergency']

    def form_valid(self, form):
        form.instance.make_by = Profile.objects.get(username=self.request.user.username)
        form.instance.save()
        return super(RealAnalysisCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('model:detail_real_analysis', kwargs={'pk': self.object.pk})


class RealAnalysisUpdateView(EventTodayProfileMixin, UpdateView):
    model = RealAnalysis
    fields = ['affections', 'measures', 'first_time', 'cause', 'summary', 'evaluation', 'emergency']
    template_name = 'emergency/real_analysis/realanalysis_form.html'

    def get_success_url(self):
        return reverse_lazy('model:detail_real_analysis', kwargs={'pk': self.object.pk})


class RealAnalysisListView(EventTodayProfileMixin, ListView):
    model = RealAnalysis
    template_name = 'emergency/real_analysis/realanalysis_list.html'


class RealAnalysisDeleteView(SuperUserRequiredMixin, DeleteView):
    model = RealAnalysis
    template_name = 'emergency/real_analysis/realanalysis_confirm_delete.html'
    success_url = reverse_lazy('model:list_real_analysis')


class RealAnalysisDetailView(EventTodayProfileMixin, DetailView):
    model = RealAnalysis
    template_name = 'emergency/real_analysis/realanalysis_detail.html'
    context_object_name = 'real_analysis'


class SimulationAnalysisCreateView(EventTodayProfileMixin, CreateView):
    # model = SimulationAnalysis
    # fields = ['summary', 'evaluation', 'is_necessary_check', 'specify', 'emergency', 'participants']
    template_name = 'emergency/simulation_analysis/simulationanalysis_form.html'
    form_class = SimulationAnalysisCreateForm

    def get_success_url(self):
        return reverse_lazy('model:detail_simulation_analysis', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.make_by = Profile.objects.get(username=self.request.user.username)
        # form.emergency.queryset = EmergencyReport.objects.filter(report__contains='s')
        form.instance.save()
        return super(SimulationAnalysisCreateView, self).form_valid(form)


class SimulationAnalysisUpdateView(EventTodayProfileMixin, UpdateView):
    model = SimulationAnalysis
    template_name = 'emergency/simulation_analysis/simulationanalysis_form.html'
    fields = ['summary', 'evaluation', 'is_necessary_check', 'specify', 'emergency', 'participants']

    def get_success_url(self):
        return reverse_lazy('model:detail_simulation_analysis', kwargs={'pk': self.object.pk})


class SimulationAnalysisDetailView(EventTodayProfileMixin, DetailView):
    model = SimulationAnalysis
    template_name = 'emergency/simulation_analysis/simulationanalysis_detail.html'


class SimulationAnalysisListView(EventTodayProfileMixin, ListView):
    model = SimulationAnalysis
    template_name = 'emergency/simulation_analysis/simulationanalysis_list.html'


class SimulationAnalysisDeleteView(SuperUserRequiredMixin, DeleteView):
    model = SimulationAnalysis
    template_name = 'emergency/simulation_analysis/simulationanalysis_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('model:list_simulation_analysis')


class CommunicationCreateView(EventTodayProfileMixin, CreateView):
    model = Communication
    form_class = CommunicationForm
    template_name = 'communication/communication_form.html'

    def get_success_url(self):
        return reverse_lazy('model:detail_communication', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.register_by = Profile.objects.get(username=self.request.user.username)
        form.instance.area = Profile.objects.get(username=self.request.user.username).area
        form.instance.save()
        return super(CommunicationCreateView, self).form_valid(form)


class CommunicationUpdateView(EventTodayProfileMixin, UpdateView):
    model = Communication
    fields = ['airport_name', 'year', 'reception_way', 'type_communication', 'contact_data', 'info_content',
              'adopted_decision', 'distribution_date', 'emission_path']
    template_name = 'communication/communication_form.html'

    def get_success_url(self):
        return reverse_lazy('model:detail_communication', kwargs={'pk': self.object.pk})


class CommunicationDetailView(EventTodayProfileMixin, DetailView):
    model = Communication
    template_name = 'communication/communication_detail.html'


class CommunicationListView(EventTodayProfileMixin, ListView):
    model = Communication
    template_name = 'communication/communication_list.html'

    def get(self, request, *args, **kwargs):
        self.queryset = Communication.objects.filter(area=Profile.objects.get(username=request.user.username).area)
        return super(CommunicationListView, self).get(request, *args, **kwargs)


class CommunicationDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Communication
    template_name = 'communication/communication_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('model:list_communication')
