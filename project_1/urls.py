from django.conf.urls import include, url
from django.contrib import admin
from booths.views import *
urlpatterns = [
    # Examples:
    # url(r'^$', 'project_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^index/$', index),
    # url(r'^$', 'my_project.views.home', name='home'),
    url(r'^home/$', home),

    url(r'^$', index),

    # url(r'^form/$', form),
]
