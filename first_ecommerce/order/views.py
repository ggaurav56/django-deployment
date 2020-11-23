from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import OrderItem,Order
from .forms import OrderCreateForm
from cart.cart import Cart

from accounts.models import Account

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'],)  
            # clear the cart
            cart.clear()
            return render(request,
                          'order/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'order/order/create.html',
                  {'cart': cart, 'form': form})

def created(self):
    return reverse('order/order/created.html')


class OrderHistory(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/order_list.html'

    def get_context_data(self, **kwargs):
        context = super(OrderHistory, self).get_context_data()
        context['order_details'] = Order.objects.filter(email=self.request.user.email)
        context['order_items'] = OrderItem.objects.all()
        return context
