from django.conf.urls import url

from bibliography.views import BibliographyCreateView, BibliographyUpdateView, BibliographyDeleteView, \
    BibliographyCGAListView, BibliographyOtherListView

urlpatterns = [
    url(r'^create/$', BibliographyCreateView.as_view(), name='create_bibliography'),
    url(r'^cga/list/$', BibliographyCGAListView.as_view(), name='list_cga_bibliography'),
    url(r'^other/list/$', BibliographyOtherListView.as_view(), name='list_other_bibliography'),
    url(r'^update/(?P<pk>[0-9]+)/$', BibliographyUpdateView.as_view(), name='update_bibliography'),
    url(r'^delete/(?P<pk>[0-9]+)/$', BibliographyDeleteView.as_view(), name='delete_bibliography'),
]
