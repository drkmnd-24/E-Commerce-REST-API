from django.urls import path

from product import views


urlpatterns = [
    path('products/', views.get_products_list, name='products-list'),
]
