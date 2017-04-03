from django.conf.urls import url

from account.views import LoginView, LogoutView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    # url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
]
