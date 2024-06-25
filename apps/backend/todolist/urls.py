from django.urls import path

from . import views

urlpatterns = [
    path('newest/' , views.ToDoItemViewSet.as_view()),
]