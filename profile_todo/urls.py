from django.urls import path

from profile_todo import views

urlpatterns = [

    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('details/<int:pk>/', views.details, name='details'),
    path('mark-done/<int:pk>', views.mark_todo_done, name='mark todo done'),

]
