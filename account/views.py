from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views import View
from django.views.generic import FormView, RedirectView, TemplateView, UpdateView, CreateView, ListView, DeleteView, \
    DetailView

from account.forms import ProfileUpdateForm, ProfileUpdatePasswordForm, ProfileCreateForm
from account.models import Profile
from bulletin.models import Bulletin
from environmental_council.models import EnvironmentalCouncil
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


class ProfileMixin(LoginRequiredMixin):
    def get_context_data(self, **kwargs):
        context = super(ProfileMixin, self).get_context_data(**kwargs)
        profile = Profile.objects.get(username=self.request.user.username)
        environmental_council = EnvironmentalCouncil.objects.all()
        context['profile'] = profile
        context['environmental_council_list'] = environmental_council
        return context


class SuperUserRequiredMixin(ProfileMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(SuperUserRequiredMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class SameUserPermissionMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if int(kwargs['pk']) == request.user.pk or self.request.user.is_superuser:
            self.can_edit = True
        else:
            self.can_edit = False
        return super(SameUserPermissionMixin, self).dispatch(request, *args, **kwargs)


class SameUserPermissionViewMixin(SameUserPermissionMixin, ProfileMixin, View):
    def dispatch(self, request, *args, **kwargs):
        temp = super(SameUserPermissionViewMixin, self).dispatch(request, *args, **kwargs)
        if self.can_edit:
            return temp
        else:
            raise PermissionDenied


class AsPermissionEditView(SameUserPermissionMixin):
    def get_context_data(self, **kwargs):
        context = super(SameUserPermissionMixin, self).get_context_data(**kwargs)
        context['can_edit'] = self.can_edit
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


class DashboardView(ProfileMixin, TemplateView):
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['event_today_list'] = Event.objects.filter(
            Q(date__day=timezone.now().day) & Q(date__month=timezone.now().month)
        )
        context['events_list'] = Event.objects.all()
        context['bulletin_list'] = Bulletin.objects.all()
        return context


class ProfileUpdateView(SameUserPermissionViewMixin, UpdateView):
    model = Profile
    template_name = 'account/profile_update_form.html'
    form_class = ProfileUpdateForm

    def get_success_url(self):
        return reverse_lazy('account:detail_user', kwargs={'pk': self.object.pk})


class ProfileUpdatePasswordView(SameUserPermissionViewMixin, UpdateView):
    model = Profile
    template_name = 'account/profile_update_password_form.html'
    form_class = ProfileUpdatePasswordForm

    def get_success_url(self):
        return reverse_lazy('account:detail_user', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        post = super(ProfileUpdatePasswordView, self).post(request, *args, **kwargs)
        user = self.object
        password = request.POST.get("password", "")
        if password:
            user.set_password(password)
            user.save()
        return post


class ProfileCreateView(SuperUserRequiredMixin, ProfileMixin, CreateView):
    model = Profile
    form_class = ProfileCreateForm
    success_url = reverse_lazy('account:list_user')

    def get_context_data(self, **kwargs):
        context = super(ProfileCreateView, self).get_context_data(**kwargs)
        context['event_today_list'] = Event.objects.filter(
            Q(date__day=timezone.now().day) & Q(date__month=timezone.now().month)
        )
        return context

    def form_valid(self, form):
        password = form.cleaned_data.get('password', '')
        user = form.save(commit=False)
        if password:
            user.set_password(password)
            user.save()
        return super(ProfileCreateView, self).form_valid(form)


class ProfileListView(SuperUserRequiredMixin, ProfileMixin, ListView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        context['event_today_list'] = Event.objects.filter(
            Q(date__day=timezone.now().day) & Q(date__month=timezone.now().month)
        )
        return context


class ProfileDetailView(AsPermissionEditView, ProfileMixin, DetailView):
    model = Profile
    context_object_name = 'prof'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['event_today_list'] = Event.objects.filter(
            Q(date__day=timezone.now().day) & Q(date__month=timezone.now().month))
        return context


class ProfileDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Profile
    success_url = reverse_lazy('account:list_user')

    def get_context_data(self, **kwargs):
        context = super(ProfileDeleteView, self).get_context_data(**kwargs)
        context["userdel"] = self.object
        return context
