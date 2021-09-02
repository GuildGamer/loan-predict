from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/', include('base.urls', namespace="base" )),
    path('api-auth/', include('rest_framework.urls'))
]
