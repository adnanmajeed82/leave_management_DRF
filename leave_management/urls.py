from django.contrib import admin
from django.urls import path, include  # Import the 'include' function
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Employee Leave Management Services API",
      default_version='v1',
      description="Plexaar API",
      terms_of_service="https://www.plexaar.com/policies/terms/",
      contact=openapi.Contact(email="adnan@setleq.net"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('leaves.urls')),  # Include the URLs from your 'leaves' app
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
