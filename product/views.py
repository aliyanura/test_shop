from rest_framework.viewsets import ModelViewSet
from .models import Category, Product
from product.serializers import CategorySerializer,\
                                ProductSerializer,\
                                ProductWriteSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related('categories', 'seller').all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ProductWriteSerializer
        return ProductSerializer
