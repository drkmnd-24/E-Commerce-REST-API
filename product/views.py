from rest_framework.generics import get_object_or_404

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
    queryset = get_object_or_404(Product, id=pk)

    serializer = ProductSerializer(queryset, many=False)
    return Response({'product': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def upload_product_images(request, pk):
    data = request.data
    files = request.FILES.getlist('images')

    return Response({'success': 'image uploaded'})
