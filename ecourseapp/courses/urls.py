from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]