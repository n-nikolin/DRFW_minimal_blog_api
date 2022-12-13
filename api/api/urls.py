from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from blog import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
