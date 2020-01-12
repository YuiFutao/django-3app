from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 空欄= 未記入（localhost:8000 とした時のを拾う）
    path('', include('todo.urls'))
]
