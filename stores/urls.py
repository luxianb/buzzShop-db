from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.products_list, name="products-list"),
    path('product/add/', views.product_add, name="product-add"),
    path('product/e/<str:pk>/', views.product_updateDelete, name="product-update"),
    path('product/<str:pk>/', views.product_view, name="product-detail"),

    path('store/', views.store_list, name="store-list"),
    path('store/add/', views.store_add, name="store-add"),
    path('store/e/<str:pk>/', views.store_updateDelete, name="store-update"),
    path('store/<str:pk>/', views.store_view, name="store-detail"),

    path('cart/add/', views.cart_add, name="cart-add"),
    path('cart/e/<str:item_id>/', views.cart_updateDelete, name="cart-update"),
    path('cart/item/<str:item_id>/', views.cart_item, name="cart-item"),
    path('cart/<str:user_id>/', views.user_cart, name="cart-list"),
]
