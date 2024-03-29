from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'title']
    pagination_class = LimitOffsetPagination
    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'products']
    ordering_fields = ['id', 'address']
    search_fields = ['products__title']
    pagination_class = LimitOffsetPagination
    # при необходимости добавьте параметры фильтрации