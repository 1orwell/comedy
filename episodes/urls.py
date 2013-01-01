from django.conf.urls import patterns, url

from episodes import views

urlpatterns = patterns('',
    url(r'^$', views.series_list),
    url(r'^list$', views.series_list),
    #url(r'^(?P<quote_id>\d+)/$', views.detail),
)
