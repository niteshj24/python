"""djangoProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from ex3.api import RouterList, RouterFilter ,RouterDetail, UserAuthentication
from ex1.views import router_view,router_list,router_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('routeradd', router_view, name='routerview'),
    path('', router_list, name='routerlist'),
    path('routeredit/<int:id>/', router_edit, name='routeredit'),
    url(r'^api/routerlist/$', RouterList.as_view(), name='routerlist'),
    url(r'^api/$', RouterList.as_view(), name='routerlist'),
    url(r'^api/routerlist/(?P<routerid>\d+)/$', RouterDetail.as_view(), name='routerlist'),
    url(r'^api/routerget/(?P<loopback>\d+)/$', RouterFilter.as_view(), name='routerget'),
    url(r'^api/auth/$', UserAuthentication.as_view(), name='UserAuthenticationAPI')

]
