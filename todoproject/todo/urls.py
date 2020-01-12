from django.urls import path, include
from .views import TodoList

urlpatterns = [
    path('list/', TodoList.as_view()),

]
