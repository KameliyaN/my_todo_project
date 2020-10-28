from django.urls import path

from profile_todo import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),

]
