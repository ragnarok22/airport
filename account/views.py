from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views import View
from django.views.generic import FormView, RedirectView, TemplateView, UpdateView, CreateView, ListView, DeleteView, \
    DetailView

from account.models import Profile
from event.models import Event


class LoginRequiredMixin(View):
    @method_decorator(login_required(login_url=reverse_lazy('account:login')))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class AnonymousRequiredMixin(View):
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('dashboard'))

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return super(AnonymousRequiredMixin, self).dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('dashboard'))


class ProfileMixin(object):

    def get_context_data(self, **kwargs):
        context = super(ProfileMixin, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(username=self.request.user.username)
        return context


class LoginView(AnonymousRequiredMixin, FormView):
    form_class = AuthenticationForm
    template_name = 'account/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('dashboard'))


class LogoutView(RedirectView):
    pattern_name = 'account:login'
    permanent = False

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class DashboardView(LoginRequiredMixin, ProfileMixin, TemplateView):
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['event_today_list'] = Event.objects.filter(
            Q(date__day=timezone.now().day) and Q(date__month=timezone.now().month)
        )
        return context


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['username', 'password', 'first_name', 'last_name', 'email', 'picture', 'born_date','sex']
    template_name = 'account/profile_update_form.html'

    def get_success_url(self):
        return reverse_lazy('account:detail_user', kwargs={'pk': self.object.pk})


class ProfileCreateView(CreateView):
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('account:list_user')

    def get_context_data(self, **kwargs):
        context = super(ProfileCreateView, self).get_context_data(**kwargs)
        context['event_list'] = Event.objects.filter(
            Q(date__day=timezone.now().day) & Q(date__month=timezone.now().month)
        )
        context['profile'] = Profile.objects.get(username=self.request.user.username)
        return context


class ProfileListView(ListView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        context['event_list'] = Event.objects.filter(
            Q(date__day=timezone.now().day) & Q(date__month=timezone.now().month)
        )
        context['profile'] = Profile.objects.get(username=self.request.user.username)
        return context


class ProfileDetailView(DetailView):
    model = Profile


class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy('account:list_user')
