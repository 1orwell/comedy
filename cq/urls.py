from django.conf.urls import patterns, url

from cq import views

urlpatterns = patterns('',
    url(r'^$', views.list),
    url(r'^random$', views.q_random),
    url(r'^list$', views.list),
    url(r'^(?P<quote_id>\d+)/$', views.detail),
)
