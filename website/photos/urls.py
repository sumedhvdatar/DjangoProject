from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.index,name='index'),
    url(r'^login/',views.login),
    url(r'^manage/',views.manage),

]