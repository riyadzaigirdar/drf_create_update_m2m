from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("post", views.PostView)
router.register("category", views.CategoryView)

urlpatterns = router.urls
    


