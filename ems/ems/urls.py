"""ems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from employ import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.verify,name='verify'),
    path('create/',views.emp_create,name='create'),
    path('profile/',views.profile,name='profile'),
    path('sal/',views.salaryview,name='view_sal'),
    path('dep/',views.departmentview,name='view_dep'),
    path('create/dep/',views.createdep,name='create_dep'),
    path('create/sal/',views.createsal,name='create_sal'),
    path('logout/',views.Logout,name="logout"),
    path('empview/',views.viewemp,name='emp_view'),
    path('empupdate/<int:pk>/',views.empupdate,name='emp_update'),
    path('empdelete/<int:pk>/',views.empdelete,name='emp_delete'),
    path('depupdate/<int:pk>/',views.updatedep,name='dep_update'),
    path('depdelete/<int:pk>/',views.deletedep,name='dep_delete'),
    path('salupdate/<int:pk>/',views.updatesal,name='sal_update'),
    path('saldelete/<int:pk>/',views.deletesal,name='sal_delete'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
