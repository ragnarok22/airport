from django.conf.urls import url

from training.views import TrainingCreateView, TrainingUpdateView, TrainingDetailView, TrainingListView, \
    TrainingDeleteView

urlpatterns = [
    url(r'^create/$', TrainingCreateView.as_view(), name='create_training'),
    url(r'^update/(?P<pk>[0-9]+)/$', TrainingUpdateView.as_view(), name='update_training'),
    url(r'^detail/(?P<pk>[0-9]+)/$', TrainingDetailView.as_view(), name='detail_training'),
    url(r'^delete/(?P<pk>[0-9]+)/$', TrainingDeleteView.as_view(), name='delete_training'),
    url('list/$', TrainingListView.as_view(), name='list_training'),
]
