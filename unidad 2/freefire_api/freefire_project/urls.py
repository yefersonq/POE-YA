from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from jugadores.views import JugadorViewSet

router = routers.DefaultRouter()
router.register(r'jugadores', JugadorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
