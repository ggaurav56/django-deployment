from django.urls import path
from cbv_app import views

app_name = 'cbv_app'

urlpatterns = [
    path('',views.BookListView.as_view(),name='list'),
    path('create/',views.BookCreateView.as_view(),name='create'),
    path('books/<int:pk>',views.BookDetailView.as_view(),name='detail'),
    path('update/<int:pk>',views.BookUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.BookDeleteView.as_view(),name='delete'),

]
