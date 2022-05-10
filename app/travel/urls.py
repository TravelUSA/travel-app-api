from django.urls import path, include
from rest_framework.routers import DefaultRouter

from travel import views

router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('itenaries', views.ItenaryViewSet)

app_name = 'travel'

urlpatterns = [
    path('', include(router.urls))
]
