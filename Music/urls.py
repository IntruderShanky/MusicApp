from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^music/', include('music.urls')),
    url(r'^admin/', admin.site.urls),
]
