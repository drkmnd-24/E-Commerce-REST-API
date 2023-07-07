from .models import Product, ProductImages

from product.api.serializers import ProductSerializer, ProductImagesSerializer
from product.api.filters import ProductFilter

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import get_object_or_404

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
def upload_product_images(request):
    data = request.data
    files = request.FILES.getlist('images')

    images = []
    for f in files:
        image = ProductImages.objects.create(product=Product(data['product']), image=f)
        images.append(image)

    serializer = ProductImagesSerializer(images, many=True)

    return Response({'uploaded': serializer.data}, status=status.HTTP_201_CREATED)
