from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('',views.ProductListView.as_view(),name='list'),
    path('product_detail/<slug:slug>',views.ProductDetailView.as_view(),name='detail')
]