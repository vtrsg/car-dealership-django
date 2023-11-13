from django.db import IntegrityError
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response

from ..models import ModelType
from ..serializers.model_serializer import ModelSerializer


class ModelViewSet(viewsets.ViewSet):
    serializer_class = ModelSerializer

    def get_queryset(self):
        return ModelType.objects.all()

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
                    'message': 'Model created successfully.',
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

    def retrieve(self, request, pk_model=None):
        try:
            query = self.get_queryset()
            model = query.get(pk=pk_model)
            serializer = self.serializer_class(model)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ModelType.DoesNotExist:
            return Response(
                {
                    'status': 'Error',
                    'message': f'Model {pk_model} not found!',
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def update(self, request, pk_model=None):
        try:
            query = self.get_queryset()
            model = query.get(pk=pk_model)
            serializer = self.serializer_class(
                model, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    'status': 'Success',
                    'message': 'Model updated successfully.',
                },
                status=status.HTTP_200_OK,
            )
        except ModelType.DoesNotExist:
            return Response(
                {
                    'status': 'Error',
                    'message': f'Model {pk_model} not found!',
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

    def destroy(self, request, pk_model=None):
        try:
            query = self.get_queryset()
            model = query.get(pk=pk_model)
            model.delete()
            return Response(
                {
                    'status': 'Success',
                    'message': f'Model {pk_model} deleted successfully.',
                },
                status=status.HTTP_200_OK,
            )
        except ModelType.DoesNotExist:
            return Response(
                {
                    'status': 'Error',
                    'message': f'Model {pk_model} not found!',
                },
                status=status.HTTP_404_NOT_FOUND,
            )
