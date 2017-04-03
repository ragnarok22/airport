from django.conf.urls import url

from model.views import ModelR01PG01CreateView, ModelR01PG01UpdateView, ModelR01PG01DetailView, ModelR01PG01ListView, \
    ModelR01PG01DeleteView

urlpatterns = [
    url(r'^create/r01pg01/$', ModelR01PG01CreateView.as_view(), name='create_modelr01pg01'),
    url(r'^update/r01pg01/(?P<pk>[0-9]+)/$', ModelR01PG01UpdateView.as_view(), name='update_modelr01pg01'),
    url(r'^detail/r01pg01/(?P<pk>[0-9]+)/$', ModelR01PG01DetailView.as_view(), name='detail_modelr01pg01'),
    url(r'^list/r01pg01/$', ModelR01PG01ListView.as_view(), name='list_modelr01pg01'),
    url(r'^delete/r01pg01/(?P<pk>[0-9]+)/$', ModelR01PG01DeleteView.as_view(), name='delete_modelr01pg01'),
]
