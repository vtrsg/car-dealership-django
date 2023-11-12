from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models import Brand
from ..serializers.brand_serializer import BrandSerializer


class BrandViewSet(viewsets.ViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk_brand=None):
        try:
            brand = self.queryset.get(pk=pk_brand)
            serializer = self.serializer_class(brand)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Brand.DoesNotExist:
            return Response(
                {
                    'status': 'Error',
                    'message': f'User {pk_brand} not found!',
                },
                status=status.HTTP_404_NOT_FOUND,
            )
