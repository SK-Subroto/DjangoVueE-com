from rest_framework import serializers
from .models import Category, Supplier, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class ProductReadSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    # supplier = SupplierSerializer(read_only=True)
    # category_name = serializers.ReadOnlyField()
    # supplier_name = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ['id', 'img', 'name', 'category', 'supplier', 'price', 'description', 'category_name', 'supplier_name']
        # fields = '__all__'
        # depth = 2


class ProductWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'supplier', 'price', 'description']

