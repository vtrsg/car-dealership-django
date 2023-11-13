from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models import Year
from ..serializers.year_serializer import YearSerializer


class YearViewSet(viewsets.ViewSet):
    serializer_class = YearSerializer
    queryset = Year.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk_year=None):
        try:
            year = self.queryset.get(pk=pk_year)
            serializer = self.serializer_class(year)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Year.DoesNotExist:
            return Response(
                {
                    'status': 'Error',
                    'message': f'Year {pk_year} not found!',
                },
                status=status.HTTP_404_NOT_FOUND,
            )
