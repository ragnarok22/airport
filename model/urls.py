from django.conf.urls import url

from model.views import ModelR01PG01CreateView, ModelR01PG01UpdateView, ModelR01PG01DetailView, ModelR01PG01ListView, \
    ModelR01PG01DeleteView, AreaCreateView, AreaUpdateView, AreaDetailView, AreaListView, AreaDeleteView, LawRequirementCreateView, \
    LawRequirementDeleteView, LawRequirementDetailView, LawRequirementListView, LawRequirementUpdateView

urlpatterns = [
    url(r'^create/r01pg01/$', ModelR01PG01CreateView.as_view(), name='create_modelr01pg01'),
    url(r'^update/r01pg01/(?P<pk>[0-9]+)/$', ModelR01PG01UpdateView.as_view(), name='update_modelr01pg01'),
    url(r'^detail/r01pg01/(?P<pk>[0-9]+)/$', ModelR01PG01DetailView.as_view(), name='detail_modelr01pg01'),
    url(r'^list/r01pg01/$', ModelR01PG01ListView.as_view(), name='list_modelr01pg01'),
    url(r'^delete/r01pg01/(?P<pk>[0-9]+)/$', ModelR01PG01DeleteView.as_view(), name='delete_modelr01pg01'),

    url(r'^create/area/$', AreaCreateView.as_view(), name='create_area'),
    url(r'^update/area/(?P<pk>[0-9]+)/$', AreaUpdateView.as_view(), name='update_area'),
    url(r'^detail/area/(?P<pk>[0-9]+)/$', AreaDetailView.as_view(), name='detail_area'),
    url(r'^list/area/$', AreaListView.as_view(), name='list_area'),
    url(r'^delete/area/(?P<pk>[0-9]+)/$', AreaDeleteView.as_view(), name='delete_area'),

    url(r'^create/law/$', LawRequirementCreateView.as_view(), name='create_law'),
    url(r'^update/law/(?P<pk>[0-9]+)/$', LawRequirementUpdateView.as_view(), name='update_law'),
    url(r'^detail/law/(?P<pk>[0-9]+)/$', LawRequirementDetailView.as_view(), name='detail_law'),
    url(r'^list/law/$', LawRequirementListView.as_view(), name='list_law'),
    url(r'^delete/law/(?P<pk>[0-9]+)/$', LawRequirementDeleteView.as_view(), name='delete_law'),

]
