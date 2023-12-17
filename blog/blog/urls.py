from django.apps import apps
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path(
        '',
        include('posts.urls', namespace=apps.get_app_config('posts').name),
    ),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'docs/',
        SpectacularSwaggerView.as_view(
            url_name='schema',
        ),
        name='swagger-ui',
    ),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
]
