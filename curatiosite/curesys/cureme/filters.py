import django_filters
from .models import *
from django_filters import DateFilter, CharFilter

# class Commfilter(django_filters.FilterSet):
#     start_date = DateFilter(field_name="cmty_est_date",lookup_expr="gte")
#     end_date = DateFilter(field_name="cmty_close_date",lookup_expr="gte")
#     comm_state = CharFilter(field_name='cmty_state', lookup_expr='icontains')
#     class Meta:
#         model = Community
#         fields = ('cmty_metric', 'cmty_name')
#         exclude = ('cmty_metric')
