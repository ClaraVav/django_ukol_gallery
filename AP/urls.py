from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^browse$', views.art_list, name='art_list'),
    url(r'^art/(?P<pk>[0-9]+)/$', views.art_detail, name='art_detail'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.cat_detail, name='cat_detail'),
    url(r'^category/new$', views.cat_create, name='cat_create'),

    url(r'^profile$', views.profile_page, name='profile_page'),
    url(r'^login$', views.log_in, name='log_in'),
    url(r'^logout$', views.log_out, name='log_out'),
    url(r'^register$', views.register, name='register'),
]
