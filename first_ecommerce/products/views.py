from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from cart.forms import CartAddProductForm


from .models import Product
# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'products'
    # cart_product_form = CartAddProductForm()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        context['cart_product_form'] = CartAddProductForm()
        return context    



    template_name = 'products/product_detail.html'
    