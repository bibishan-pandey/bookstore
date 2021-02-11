"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


schema_view = get_schema_view(
    openapi.Info(
        title='Book Store API',
        default_version='v1',
        description='API Description',
        terms_of_service='https://www.bookstore.com/policies/terms/',
        contact=openapi.Contact(email='contact@bookstore.local'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger
    path(
        '', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'redoc/', schema_view.with_ui(
            'redoc',
            cache_timeout=0,
        ), name='schema-redoc',
    ),

    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('django.contrib.auth.urls')),

    # Django rest framework
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
    path('api/token/verify/', verify_jwt_token),

    # Local apps
    path('accounts/', include('users.urls')),
    path('pages/', include('pages.urls')),
]
