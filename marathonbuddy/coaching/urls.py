from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('try_a_text/', views.try_a_text),
    path('send_text/', views.send_text),
    path('who_are_you/', views.who_are_you),
    path('what_is_this/', views.what_is_this),
    path('races/', views.races),
    path('sms/', views.sms_interaction),
    path('add_cheer/', views.add_cheer)
]