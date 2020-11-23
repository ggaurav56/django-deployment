from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    path('create/',views.order_create,name = 'order_create'),
    path('created/',views.order_create,name = 'created'),
    path('order_list/',views.OrderHistory.as_view(),name='order_list'),
]