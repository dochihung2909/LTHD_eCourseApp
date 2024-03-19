from django.urls import include, path, re_path
from . import views
from rest_framework import routers


r = routers.DefaultRouter()

r.register('categories', views.CategoryViewSet, basename='categories')
r.register('courses', views.CourseViewSet, basename='courses')
r.register('lessons', views.LessonViewSet, basename='lessons')



urlpatterns = [
    path('', include(r.urls)),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls'))
]
