from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from news import views



urlpatterns = patterns('',
	#url(r'^$', views.index, name='index'),
	url(r'^feeds/$',views.feeds, name='feeds'),
	url(r'^login/$',views.login_view, name='login'),
	url(r'^signup/$', views.register, name='signup'),

)
