from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from api.views.users import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')

schema_view = get_swagger_view(title='Tukole API')

urlpatterns = [
    path('docs/', schema_view),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
