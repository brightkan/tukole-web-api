from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views.users import UserViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, base_name='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
