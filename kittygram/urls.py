from django.urls import include, path
from rest_framework.routers import SimpleRouter, DefaultRouter
from cats.views import CatViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
