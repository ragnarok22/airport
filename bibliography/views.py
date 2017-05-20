from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from account.views import SuperUserRequiredMixin, ProfileMixin
from bibliography.models import Bibliography


class BibliographyCreateView(SuperUserRequiredMixin, CreateView):
    model = Bibliography
    fields = '__all__'

    def form_valid(self, form):
        document_type = form.cleaned_data.get('document_type', '')
        if document_type == 'CGA':
            self.success_url = reverse_lazy('bibliography:list_cga_bibliography')
        else:
            self.success_url = reverse_lazy('bibliography:list_other_bibliography')
        return super(BibliographyCreateView, self).form_valid(form)


class BibliographyUpdateView(SuperUserRequiredMixin, UpdateView):
    model = Bibliography
    fields = '__all__'
    success_url = reverse_lazy('dashboard')


class BibliographyCGAListView(ProfileMixin, ListView):
    model = Bibliography
    queryset = Bibliography.objects.filter(document_type='CGA')

    def get_context_data(self, **kwargs):
        context = super(BibliographyCGAListView, self).get_context_data(**kwargs)
        context['header'] = 'Documentos del Consejo de Gestion Ambiental'
        return context


class BibliographyOtherListView(ProfileMixin, ListView):
    model = Bibliography
    queryset = Bibliography.objects.filter(document_type='Otros')

    def get_context_data(self, **kwargs):
        context = super(BibliographyOtherListView, self).get_context_data(**kwargs)
        context['header'] = 'Otras Bibliografias'
        return context


class BibliographyDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Bibliography
    success_url = reverse_lazy('dashboard')

    def delete(self, request, *args, **kwargs):
        document_type = request.POST.get('document_type', '')
        if document_type == 'CGA':
            self.success_url = reverse_lazy('bibliography:list_cga_bibliography')
        else:
            self.success_url = reverse_lazy('bibliography:list_other_bibliography')
        return super(BibliographyDeleteView, self).delete(request, *args, **kwargs)
