from django.urls import path

from .views import brand_view, car_view, model_view, user_view, year_view

app_name = 'api'

urlpatterns = [
    path(
        'user/create/',
        user_view.CustomUserCreate.as_view(),
        name='create_user',
    ),
    path(
        'logout/blacklist/',
        user_view.BlacklistTokenUpdateView.as_view(),
        name='blacklist',
    ),
    path(
        'cars/',
        car_view.CarViewSet.as_view({'post': 'create', 'get': 'list'}),
        name='cars',
    ),
    path(
        'cars/<pk_car>/',
        car_view.CarViewSet.as_view(
            {
                'put': 'update',
                'patch': 'update',
                'delete': 'destroy',
                'get': 'retrieve',
            }
        ),
        name='car_detail',
    ),
    path(
        'brands/',
        brand_view.BrandViewSet.as_view({'get': 'list'}),
        name='brands',
    ),
    path(
        'brands/<pk_brand>/',
        brand_view.BrandViewSet.as_view({'get': 'retrieve'}),
        name='brand_detail',
    ),
    path(
        'years/',
        year_view.YearViewSet.as_view({'get': 'list'}),
        name='years',
    ),
    path(
        'years/<pk_year>/',
        year_view.YearViewSet.as_view({'get': 'retrieve'}),
        name='year_detail',
    ),
    path(
        'models/',
        model_view.ModelViewSet.as_view({'post': 'create', 'get': 'list'}),
        name='models',
    ),
    path(
        'models/<pk_model>/',
        model_view.ModelViewSet.as_view(
            {
                'put': 'update',
                'patch': 'update',
                'delete': 'destroy',
                'get': 'retrieve',
            }
        ),
        name='model_detail',
    ),
]
