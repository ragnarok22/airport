from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from account.models import Profile
from account.views import ProfileMixin, SuperUserRequiredMixin
from audit.models import Audit, GeneralProgramAudit
from audit.forms import AuditForm


class GeneralProgramAuditListView(ProfileMixin, ListView):
    template_name = 'audit/general_program_list.html'
    model = GeneralProgramAudit
    context_object_name = 'general_program_list'

    def get_context_data(self, **kwargs):
        context = super(GeneralProgramAuditListView, self).get_context_data(**kwargs)
        context['audit_list'] = Audit.objects.all()
        return context


class GeneralProgramAuditUpdateView(SuperUserRequiredMixin, UpdateView):
    model = GeneralProgramAudit
    fields = ['observations', 'made_by']
    template_name = 'audit/general_program_form.html'

    def get_success_url(self):
        return reverse_lazy('audit:detail_general_program', kwargs={'pk': self.object.pk})


class GeneralProgramAuditCreateView(SuperUserRequiredMixin, CreateView):
    model = GeneralProgramAudit
    fields = ['observations']
    template_name = 'audit/general_program_form.html'

    def get_success_url(self):
        return reverse_lazy('audit:detail_general_program', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.made_by = Profile.objects.get(username=self.request.user.username)
        form.instance.save()
        return super(GeneralProgramAuditCreateView, self).form_valid(form)


class GeneralProgramAuditDetailView(ProfileMixin, DetailView):
    template_name = 'audit/general_program_detail.html'
    model = GeneralProgramAudit
    context_object_name = 'general_program'

    def get_context_data(self, **kwargs):
        context = super(GeneralProgramAuditDetailView, self).get_context_data(**kwargs)
        context['audit_list'] = Audit.objects.filter(general_program=self.object)
        return context


class GeneralProgramAuditDeleteView(SuperUserRequiredMixin, DeleteView):
    model = GeneralProgramAudit

    def get_success_url(self):
        return reverse_lazy('audit:list_general_program')


class AuditCreateView(SuperUserRequiredMixin, CreateView):
    model = Audit
    form_class = AuditForm
    success_url = reverse_lazy('audit:list_general_program')

    def form_valid(self, form):
        form.instance.general_program = GeneralProgramAudit.objects.get(pk=self.kwargs['pk'])
        form.instance.save()
        return super(AuditCreateView, self).form_valid(form)


class AuditUpdateView(SuperUserRequiredMixin, UpdateView):
    model = Audit
    form_class = AuditForm

    def get_success_url(self):
        return reverse_lazy('audit:detail_general_program', kwargs={'pk': self.object.general_program.pk})


class AuditDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Audit
    success_url = reverse_lazy('audit:list_general_program')
