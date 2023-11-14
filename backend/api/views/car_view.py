from django.db import IntegrityError
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response


from ..models import Car
from ..serializers.car_serializer import CarSerializer
from ..utils.permission import IsOwnerOrReadOnly

class CarViewSet(viewsets.ViewSet):
    serializer_class = CarSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Car.objects.all()

    def list(self, request):
        query = self.get_queryset()
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    'status': 'Success',
                    'message': 'Car created successfully!!',
                },
                status=status.HTTP_201_CREATED,
            )
        except serializers.ValidationError as e:
            return Response(
                {
                    'status': 'Error',
                    'message': 'Mandatory fields not filled in or invalid values.',
                    'errors': e.detail,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except IntegrityError as e:
            return Response(
                {
                    'status': 'Error',
                    'message': str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, pk_car=None):
        try:
            query = self.get_queryset()
            car = query.get(pk=pk_car)
            serializer = self.serializer_class(car)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Car.DoesNotExist:
            return Response(
                {
                    'status': 'Error',
                    'message': f'Car {pk_car} not found!',
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def update(self, request, pk_car=None):
        try:
            query = self.get_queryset()
            car = query.get(pk=pk_car)
            serializer = self.serializer_class(
                car, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    'status': 'Success',
                    'message': 'Car updated successfully.',
                },
                status=status.HTTP_200_OK,
            )
        except Car.DoesNotExist:
            return Response(
                {
                    'status': 'Error',
                    'message': f'Car {pk_car} not found!',
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        except serializers.ValidationError as e:
            return Response(
                {
                    'status': 'Error',
                    'message': 'Mandatory fields not filled in or invalid values.',
                    'errors': e.detail,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except IntegrityError as e:
            return Response(
                {
                    'status': 'Error',
                    'message': str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def destroy(self, request, pk_car=None):
        try:
            query = self.get_queryset()
            car = query.get(pk=pk_car)
            car.delete()
            return Response(
                {
                    'status': 'Success',
                    'message': f'Car {pk_car} deleted successfully.',
                },
                status=status.HTTP_200_OK,
            )
        except Car.DoesNotExist:
            return Response(
                {
                    'status': 'Error',
                    'message': f'Car {pk_car} not found!',
                },
                status=status.HTTP_404_NOT_FOUND,
            )
