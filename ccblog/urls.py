from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ccblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.home'),
    # url(r'^(?P<my_args>\d+)/$', 'article.views.detail', name = 'detail'),
    # url(r'^temp/$', 'article.views.temp'),
    # url(r'^bootstrap/$', 'article.views.bootstrap'),
]
