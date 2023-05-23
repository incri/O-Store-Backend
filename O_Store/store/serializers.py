from rest_framework import serializers
from .models import Product, Collection
from decimal import Decimal

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only = True)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title','description', 'price','price_with_tax', 'collection', 'inventory', 'slug']
     
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")


    def calculate_tax(self, product: Product):
        return product.price* Decimal(1.1)