from .views import url_view, redirect_url_view
from .views import URLViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = "urlshortener"

urlpatterns = [
    path("", url_view, name="form-view"),
    path('<str:short_url>', redirect_url_view, name='redirect'),
]

router = DefaultRouter()
router.register("api/short-url", URLViewSet, basename="api")

urlpatterns += router.urls