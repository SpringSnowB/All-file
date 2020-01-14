"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

#该配置项将子行而下逐一匹配 若某行配置上，则终止向下匹配行为
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index_view),
    # http://127.0.0.1:8000/page1
    url(r'^page1$', views.page1_view),
    #http://127.0.0.1:8000/page2
    url(r'^page2$', views.page2_view),
    url(r'^page(\d+)',views.pagen_view),
    url(r'^(\d+)/(\w+)/(\d+)',views.acl_view),
    url(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})',views.person_view),
    url(r'^birthday/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})',views.birthday_view),
    url(r'^birthday/(?P<day>\d{1,2})/(?P<month>\d{1,2})/(?P<year>\d{4})',views.birthday_view),
    url(r'^test_get$',views.test_get),
    url(r'^test_get_server$',views.test_get_server),
]
