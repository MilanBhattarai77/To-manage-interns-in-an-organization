from myapp.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls

# from django.urls import path
# from rest_framework.routers import DefaultRouter # type: ignore
# from .views import UserViewSet





# list = UserViewSet.as_view({'get': 'list'})
# detail = UserViewSet.as_view({'get': 'retrieve'})




# urlpatterns = [
#     path('users/', list, name='list'),
#     path('users/<int:pk>/', detail, name='detail'),
# ]
