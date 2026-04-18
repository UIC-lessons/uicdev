from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("common/", include("apps.common.urls")),
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("notification/", include("apps.notifications.urls")),
    path("interaction/", include("apps.interactions.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("courses/", include("apps.courses.urls")),
    path('i18n/', include('django.conf.urls.i18n')),
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path('rosetta/', include('rosetta.urls')),
    ]