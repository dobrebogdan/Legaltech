from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getlaws', views.get_laws, name='get_laws')
]