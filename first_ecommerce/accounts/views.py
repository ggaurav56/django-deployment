from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy

from .models import Account,Address
from .forms import RegistrationForm, AddressCreateForm
from products.models import Product

# for password change
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required



class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('products:list')
        if next_url:
            success_url += '?next={}'.format(next_url)

        return success_url


class ProfileView(UpdateView):
    model = Account
    fields = ['email','name', 'phone',]
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse('accounts:login')

    def get_object(self):
        return self.request.user



#change user password
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


#add to favorite
@login_required
def favorite_add(request, id):
    product = get_object_or_404(Product, id=id)
    if product.favorites.filter(id=request.user.id).exists():
        product.favorites.remove(request.user)
    else:
        product.favorites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

#view favourites
class FavoriteListView(ListView, LoginRequiredMixin):
    model = Account
    template_name = 'registration/favorites.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favorites'] = Account.objects.filter(email=self.request.user.email)
        return context


#views related to address model
class AddressCreateView(CreateView, LoginRequiredMixin):
    model = Address
    template_name = 'accounts/create_address.html'
    fields = ['full_name','phone','address1','address2','postal_code','city','state',]

    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.account = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:address_list')

class AddressListView(ListView,LoginRequiredMixin):
    model = Address
    template_name = 'accounts/address_list.html'
    context_object_name = 'address_list' 


    def get_queryset(self, *args, **kwargs): 
        qs = super(AddressListView, self).get_queryset(*args, **kwargs) 
        # qs = Address.objects.filter(email=self.request.user.email)
        qs = qs.order_by("-id") 
        return qs.filter(account=self.request.user)


class AddressDeleteView(DeleteView, LoginRequiredMixin):
    model = Address
    success_url = reverse_lazy('accounts:address_list')

    def get_queryset(self, *args, **kwargs): 
        qs = super(AddressDeleteView, self).get_queryset(*args, **kwargs) 
        qs = qs.order_by("-id") 
        return qs.filter(account=self.request.user)

class AddressUpdateView(UpdateView):
    model = Address
    template_name = 'accounts/create_address.html'
    fields = ['full_name','phone','address1','address2','postal_code','city','state',]

    def get_success_url(self):
        return reverse('accounts:address_list')

    def get_queryset(self, *args, **kwargs): 
        qs = super(AddressUpdateView, self).get_queryset(*args, **kwargs)     
        qs = qs.order_by("-id") 
        return qs.filter(account=self.request.user)