from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from news import views


urlpatterns = [
	url(r'^$', views.feeds, name='feeds'),
	url(r'^discussion/$',views.discussion, name='discussion'),
	url(r'^login/$',views.login_view, name='login'),
	url(r'^signup/$', views.register, name='signup'),
	url(r'^discussion/comments/$',views.comment, name='comment'),	
	url(r'^logout/$',auth_views.logout,{'next_page':'/news/'}, name='logout'),
	url(r'^discussion/comment_save/$',views.comment_save, name='comment_save'),
	url(r'^profile/(?P<username>[a-zA-Z0-9]+)$', views.profile),
]
