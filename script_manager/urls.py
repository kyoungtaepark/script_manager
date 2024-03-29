# -*- coding: utf-8 -*-
"""script_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^manager/', include('manager.urls')),
    url(r'^$', RedirectView.as_view(url='/manager', permanent=True)),
    #url(r'^rest-api/',include('rest_framework.urls')),
    #url(r'^rest-swagger/', include('rest_framework_swagger.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
