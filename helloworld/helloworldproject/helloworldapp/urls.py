from django.urls import path, include
from .views import hellofunction

urlpatterns = [
  # hello でappに転送された後の処理
  path('world/', hellofunction),
]

