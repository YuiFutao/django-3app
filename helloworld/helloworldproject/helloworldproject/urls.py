from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # urlのつなぎこみ(appに転送する)
    path('hello/', include('helloworldapp.urls'))

]
