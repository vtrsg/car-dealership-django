from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models import ModelType
from ..serializers.model_serializer import ModelSerializer


class ModelViewSet(viewsets.ViewSet):
    serializer_class = ModelSerializer
    queryset = ModelType.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk_model=None):
        try:
            model = self.queryset.get(pk=pk_model)
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
