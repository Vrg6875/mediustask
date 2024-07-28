
from django.contrib import admin
from django.urls import path

from .views import*
from core import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet,studentapi,postget
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'student_data', StudentViewSet, basename='student_data')




urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('core/',views.core,name='core'),
    # path('vrg/',views.vrg,name='vrg'),
    # path('vicky/',views.vicky,name='vicky'),
    # path('prince/',views.prince,name='prince'),
    # path('update_student/<id>/',views.update_student,name='update_student'),
    # path('delete_student/<id>/',views.delete_student,name='delete_student'),


    # path('get_book/',views.get_book,name='get_book'),
    path('postget/',views.postget,name='vv'),
    path('patch_todo/',views.patch_todo,name='patch_todo'),
    path('student/',views.studentapi.as_view(),name='apiview'),

    path('token/', obtain_auth_token, name='api_token_auth'),

]
