from django.conf.urls import url

from account.views import LoginView, LogoutView, ProfileCreateView, ProfileDeleteView, ProfileListView, \
    ProfileUpdateView, ProfileDetailView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^create/$', ProfileCreateView.as_view(), name='create_user'),
    url(r'^list/$', ProfileListView.as_view(), name='list_user'),
    url(r'^update/(?P<pk>[0-9]+)/$', ProfileUpdateView.as_view(), name='update_user'),
    url(r'^detail/(?P<pk>[0-9]+)/$', ProfileDetailView.as_view(), name='detail_user'),
    url(r'^delete/(?P<pk>[0-9]+)/$', ProfileDeleteView.as_view(), name='delete_user'),

]
