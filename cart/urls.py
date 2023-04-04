from django.urls import path

from cart import views

app_name = 'Cart'
urlpatterns = [
    path('add-to-cart/<int:pk>', views.add_to_cart , name='add_to_cart'),
    path('cart-item', views.cart_view , name='cart'),
    path('cart-item-delete/<int:pk>', views.delete , name='delete'),
    path('cart-confirm', views.final_order , name='cart_confirm'),
    path('order-list', views.OrderList.as_view() , name='order_list'),
    path('order-detail/<str:invoice_number>', views.OrderDetail.as_view() , name='order_detail'),

  
]






