from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from person import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'person', views.UserViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls), name='router'),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),

    # Use the `get_schema_view()` helper to add a `SchemaView` to project URLs.
    #   * `title` and `description` parameters are passed to `SchemaGenerator`.
    path('openapi', get_schema_view(
        title="Lab1",
        description="Try to learn",
        version="1.0.0"
    ), name='openapi-schema'),
    
    # Route TemplateView to serve Swagger UI template.
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]