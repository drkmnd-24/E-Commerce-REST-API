from django.urls import path

from product import views


urlpatterns = [
    path('products/', views.get_products_list, name='products-list'),
    path('products/create/', views.new_product, name='product-create'),
    path('products/<int:pk>/', views.get_product_details, name='products-detail'),
    path('products/<int:pk>/update', views.update_product, name='products-updates'),
    path('products/<int:pk>/delete', views.delete_product, name='products-delete'),
    path('products/upload_images/', views.upload_product_images, name='upload_product_images'),
]
