from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views
from accounts.views import RegistrationView, ProfileView, FavoriteListView, AddressCreateView, AddressListView, AddressDeleteView, AddressUpdateView
app_name = 'accounts'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('change_password/', views.change_password, name='change_password'),

    path('fav/<int:id>/',views.favorite_add, name='favorite_add'),
    path('accounts/favorites/',FavoriteListView.as_view(), name='favorite_list'),

    path('accounts/create_address/',AddressCreateView.as_view(),name='create_address'),
    path('accounts/address_list/',AddressListView.as_view(),name='address_list'),
    path('delete/<int:pk>',AddressDeleteView.as_view(),name='address_delete'),
    path('address_update/<int:pk>',AddressUpdateView.as_view(),name='address_update'),


]