from django.urls import include, path, re_path
from django.contrib import admin
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from blog import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # The CKEditor path
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)