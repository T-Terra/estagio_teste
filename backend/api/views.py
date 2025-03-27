from django.http import JsonResponse
from rest_framework.viewsets import ViewSet


class Api(ViewSet):
    def list(request):
        return JsonResponse({"message": "Pagina home"})