from django.conf.urls import url

from dangerous_waste.views import DangerousWasteCreateView, DangerousWasteListView, DangerousWasteDeleteView, \
    DangerousWasteDetailView, DangerousWasteUpdateView

urlpatterns = [
    url(r'^dangerous/waste/create/$', DangerousWasteCreateView.as_view(), name='create_dangerous_waste'),
    url(r'^dangerous/waste/list/$', DangerousWasteListView.as_view(), name='list_dangerous_waste'),
    url(r'^dangerous/waste/delete/(?P<pk>[0-9]+)/$', DangerousWasteDeleteView.as_view(), name='delete_dangerous_waste'),
    url(r'^dangerous/waste/detail/(?P<pk>[0-9]+)/$', DangerousWasteDetailView.as_view(), name='detail_dangerous_waste'),
    url(r'^dangerous/waste/update/(?P<pk>[0-9]+)/$', DangerousWasteUpdateView.as_view(), name='update_dangerous_waste'),
]
