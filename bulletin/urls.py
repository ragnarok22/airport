from django.conf.urls import url

from bulletin.views import BulletinCreateView, BulletinListView, BulletinUpdateView, BulletinDeleteView

urlpatterns = [
    url(r'create/$', BulletinCreateView.as_view(), name='create_bulletin'),
    url(r'list/$', BulletinListView.as_view(), name='list_bulletin'),
    url(r'update/(?P<pk>[0-9]+)/$', BulletinUpdateView.as_view(), name='update_bulletin'),
    url(r'delete/(?P<pk>[0-9]+)/$', BulletinDeleteView.as_view(), name='delete_bulletin'),
]
