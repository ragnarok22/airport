from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from account.views import DashboardView
from airport import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('account.urls', namespace='account')),
    url(r'^event/', include('event.urls', namespace='event')),
    url(r'^model/', include('model.urls', namespace='model')),
    url(r'^picture/', include('picture.urls', namespace='picture')),
    url(r'^audit/', include('audit.urls', namespace='audit')),
    url(r'^waste/', include('dangerous_waste.urls', namespace='waste')),
    url(r'^poll/', include('poll.urls', namespace='poll')),
    url(r'^bulletin/', include('bulletin.urls', namespace='bulletin')),
    url(r'^training/', include('training.urls', namespace='training')),
    url(r'^$', DashboardView.as_view(), name='dashboard'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
