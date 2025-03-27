from django_filters import FilterSet
from .models import Enterprise

class EnterpriseFilters(FilterSet):
    class Meta:
        model = Enterprise
        fields = {
            "razao_social" : ["icontains"] # url?razao_social__icontains
        }