from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import OrderItem, Product, Collection, Review
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer
from rest_framework import status
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
class ProductViewSet(ModelViewSet):
   
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        if OrderItem.object.filter(product_id=kwargs['pk']).count() > 0:
            return Response(
                {"error": "Cannot delete product. Product associated with order"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().destroy(request, *args, **kwargs)
    
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count("products")).all()
    serializer_class = CollectionSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(
                Collection.objects.annotate(products_count=Count("products")), pk=pk
            )
        if collection.products.count() > 0:
            return Response(
                {
                    "error": "Cannot delete collection. Collection associated with product "
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ReviewViewSet(ModelViewSet):

    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs['product_pk'])

    serializer_class = ReviewSerializer

    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}