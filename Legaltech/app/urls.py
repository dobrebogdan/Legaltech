from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getlaws', views.get_laws, name='get_laws'),
    path('getcases', views.get_cases, name='get_cases'),
    path('getclassification', views.get_classification, name='get_classification'),
    path('setlang', views.set_language, name='set_language')
]
