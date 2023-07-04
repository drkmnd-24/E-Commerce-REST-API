from .models import Product
from product.api.serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status


@api_view(['GET'])
def get_products_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
