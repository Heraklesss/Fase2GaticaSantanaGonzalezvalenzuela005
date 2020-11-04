from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('steam/', views.steam, name='steam'),
    path('origin', views.origin, name='origin'),
    path('wallet2', views.wallet2, name='wallet2'),
    path('preguntas', views.preguntas, name='preguntas'),
    path('contacto', views.contacto, name='contacto'),
    path('red', views.red, name='red'),
    path('fallguys', views.fallguys, name='fallguys')
]