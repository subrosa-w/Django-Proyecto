#from django.config.urls import url
from django.urls import path
from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    path('login', views.login, name='login'),
    path('seccion_perros', views.seccion_perros, name='seccion_perros'),
    path('seccion_gatos', views.seccion_gatos, name='seccion_gatos'),
    path('gato1', views.gato1, name='gato1'),
    path('gato2', views.gato2, name='gato2'),
    path('gato3', views.gato3, name='gato3'),
    path('perro1', views.perro1, name='perro1'),
    path('perro2', views.perro2, name='perro2'),
    path('perro3', views.perro3, name='perro3')
]