from rest_framework import serializers

from product.models import Product, ProductImages


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True, 'allow_blank': False},
            'price': {'required': True, 'allow_blank': False},
            'brand': {'required': True, 'allow_blank': False},
            'category': {'required': True, 'allow_blank': False},
            'stock': {'required': True, 'allow_blank': False},
        }
