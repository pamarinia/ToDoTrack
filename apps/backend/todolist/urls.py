from django.urls import path

from . import views

urlpatterns = [
    path('tasks' , views.TaskViewSet.as_view()),
    path('tasks/<int:pk>/', views.DetailTaskViewSet.as_view())
]