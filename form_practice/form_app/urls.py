from django.urls import path
from form_app import views

app_name = 'form_app'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('index/',views.index,name='index'),
    path('register',views.register,name='index'),
]
