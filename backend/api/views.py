from .models import Enterprise
from .serializer import EnterpriseSerializer
from .filters import EnterpriseFilters
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class ApiViewset(ViewSet):
    def list(self, request):
        queryset = Enterprise.objects.all()
        query_filter = EnterpriseFilters(request.GET, queryset)
        serializer = EnterpriseSerializer(query_filter.qs, many=True)
        return Response(serializer.data)