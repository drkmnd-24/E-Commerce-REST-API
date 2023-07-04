from django.urls import path

from product import views


urlpatterns = [
    path('products/', views.get_products_list, name='products-list'),
    path('products/<int:pk>/', views.get_product_details, name='products-detail'),
]
