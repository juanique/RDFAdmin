from django.conf.urls.defaults import *
from rdfadmin.handlers import saved_query_resource, recent_query_resource
import views


urlpatterns = patterns('',
    (r'^query/$', views.home),
    (r'^explore/',views.explore),
    (r'^proxy/', views.proxy),
    url(r'SavedQuery/', saved_query_resource),
    url(r'RecentQuery/', recent_query_resource),
)
