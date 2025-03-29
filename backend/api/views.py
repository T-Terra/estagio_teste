from .models import Enterprise
from .serializer import EnterpriseSerializer
from .filters import EnterpriseFilters
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND


class ApiViewset(ViewSet):
    def list(self, request):
        queryset = Enterprise.objects.all()
        query_filter = EnterpriseFilters(request.GET, queryset)
        serializer = EnterpriseSerializer(query_filter.qs[:10], many=True)
        if len(serializer.data) == 0:
            return Response(serializer.data, status=HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.data, status=HTTP_200_OK)