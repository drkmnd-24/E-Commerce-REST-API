from .models import Product
from product.api.serializers import ProductSerializer
from product.api.filters import ProductFilter

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from rest_framework import status


@api_view(['GET'])
def get_products_list(request):
    filterset = ProductFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    count = filterset.qs.count()
    resPerPage = 1
    paginator = PageNumberPagination()
    paginator.page_size = resPerPage
    queryset = paginator.paginate_queryset(filterset.qs, request)
    serializer = ProductSerializer(queryset, many=True)
    return Response({'product': serializer.data, 'count': count, 'resPerPage': resPerPage}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_product_details(request, pk):
    try:
        queryset = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'product does not exist'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(queryset)
    return Response(serializer.data, status=status.HTTP_200_OK)
