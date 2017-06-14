from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from news import views


urlpatterns = [
	url(r'^$', views.feeds, name='feeds'),
	url(r'^discussion/$',views.discussion, name='discussion'),
	url(r'^login/$',views.login_view, name='login'),
	url(r'^signup/$', views.register, name='signup'),
	
]
