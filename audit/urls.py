from django.conf.urls import url

from audit.views import GeneralProgramAuditListView, GeneralProgramAuditDetailView, GeneralProgramAuditCreateView, \
    GeneralProgramAuditUpdateView, GeneralProgramAuditDeleteView

urlpatterns = [
    url(r'^general/program/create/$', GeneralProgramAuditCreateView.as_view(),
        name='create_general_program'),
    url(r'^general/program/update/(?P<pk>[0-9]+)/$', GeneralProgramAuditUpdateView.as_view(),
        name='update_general_program'),
    url(r'^general/program/detail/(?P<pk>[0-9]+)/$', GeneralProgramAuditDetailView.as_view(),
        name='detail_general_program'),
    url(r'^general/program/list/$', GeneralProgramAuditListView.as_view(), name='list_general_program'),
    url(r'^general/program/delete/(?P<pk>[0-9]+)/$', GeneralProgramAuditDeleteView.as_view(),
        name='delete_general_program'),
]
