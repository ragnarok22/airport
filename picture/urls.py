from django.conf.urls import url

from picture.views import PictureCreateView, PictureListView, PictureDeleteView

urlpatterns = [
    url(r'^create/$', PictureCreateView.as_view(), name='create_picture'),
    url(r'^list/$', PictureListView.as_view(), name='list_picture'),
    url(r'^delete/(?P<pk>[0-9]+)/$', PictureDeleteView.as_view(), name='delete_picture'),
]
