from django.urls import path

from cart import views

app_name = 'Cart'
urlpatterns = [
    path('add-to-cart/<int:pk>', views.add_to_cart , name='add_to_cart'),
    path('cart-item', views.CartItemList.as_view() , name='cart'),
]






