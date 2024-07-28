from django.contrib import admin
from django.urls import path
from home import views
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import iplViewSet
router = DefaultRouter()
router.register(r'ipl', iplViewSet, basename='ipl_data')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('ipl_get/', views.ipl_get, name='ipl_get'),
    path('ipl_post/', views.ipl_post, name='ipl_post'),
    path('ipl_patch/<id>/', views.ipl_patch, name='ipl_patch'),
    path('ipl_delete/<id>/', views.ipl_delete, name='ipl_delete'),

    path('ipldata/',views.iplapi.as_view(),name='iplview'),
]
