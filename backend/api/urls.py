from django.urls import path

from .views.brand_view import BrandViewSet
from .views.user_view import UserViewSet

app_name = 'api'

urlpatterns = [
    path(
        'users/',
        UserViewSet.as_view({'post': 'create', 'get': 'list'}),
        name='users',
    ),
    path(
        'users/<pk_user>/',
        UserViewSet.as_view(
            {
                'put': 'update',
                'patch': 'update',
                'delete': 'destroy',
                'get': 'retrieve',
            }
        ),
        name='user_detail',
    ),
    path(
        'brands/',
        BrandViewSet.as_view({'get': 'list'}),
        name='brands',
    ),
    path(
        'brands/<pk_brand>/',
        BrandViewSet.as_view({'get': 'retrieve'}),
        name='brand_detail',
    ),
]
