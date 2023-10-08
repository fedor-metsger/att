
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from chain.models import Factory, Retailer, Entrepreneur
from chain.permissions import ActiveStaffPermission
from chain.serializers import FactorySerializer, RetailerSerializer, EntrepreneurSerializer


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all().order_by("id")
    serializer_class = FactorySerializer
    permission_classes = [ActiveStaffPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.all().order_by("id")
    serializer_class = RetailerSerializer
    permission_classes = [ActiveStaffPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


class EntrepreneurViewSet(viewsets.ModelViewSet):
    queryset = Entrepreneur.objects.all().order_by("id")
    serializer_class = EntrepreneurSerializer
    permission_classes = [ActiveStaffPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
