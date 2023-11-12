from django.urls import path

from .views.brand_view import BrandViewSet
from .views.model_view import ModelViewSet
from .views.user_view import UserViewSet
from .views.year_view import YearViewSet

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
    path(
        'years/',
        YearViewSet.as_view({'get': 'list'}),
        name='years',
    ),
    path(
        'years/<pk_year>/',
        YearViewSet.as_view({'get': 'retrieve'}),
        name='year_detail',
    ),
    path(
        'models/',
        ModelViewSet.as_view({'get': 'list'}),
        name='models',
    ),
    path(
        'models/<pk_model>/',
        ModelViewSet.as_view({'get': 'retrieve'}),
        name='model_detail',
    ),
]
