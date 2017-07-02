from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
urlpatterns = [
    # Examples:
    # url(r'^$', 'newsapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(url='news/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls')),
]
