from django.conf.urls import url
from django.contrib import admin

from posts.views import post_list, post_detail, post_update, post_create

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<slug>[\w\-]+)/$', post_detail, name='detail'),  
    url(r'^(?P<slug>[\w\-]+)/edit/$', post_update, name='update'),
    
]
