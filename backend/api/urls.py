from django.urls import path

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
]
