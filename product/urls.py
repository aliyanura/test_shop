from django.urls import path
from product.views import product_crud_view,\
                          CategoryViewSet,\
                          ProductListCreateView,\
                          ProductRetrieveUpdateDestroyView


urlpatterns = [
    path('categories/', CategoryViewSet.as_view(), name='category-list'),
    path('crud/', product_crud_view, name='product-crud'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
]
