from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_path, name='path'),
    path('upload/', views.get_file, name='file'),
    path('test/', views.Test.as_view(), name='test')
]