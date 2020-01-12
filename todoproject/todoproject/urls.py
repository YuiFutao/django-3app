from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 空欄にしておくと、ワイルドカードの扱いになる
    path('', include('todo.urls'))
]
