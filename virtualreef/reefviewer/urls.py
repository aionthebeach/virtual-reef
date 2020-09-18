from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('syncUpc', views.syncUpc, name='syncUpc'),
    path('syncInvert', views.syncInvert, name='syncInvert')
]

