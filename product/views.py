from django.shortcuts import render
from rest_framework import generics
from product.models import Category, Product
from product.serializers import CategorySerializer,\
                                ProductSerializer


def product_crud_view(request):
    return render(request, 'product_crud.html')


class CategoryViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
