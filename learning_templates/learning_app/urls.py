from learning_app import views
from django.urls import path

#template tagging
app_name = 'learning_app'

urlpatterns = [
    path('relative_url_templates/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
    path('index/',views.index,name='index'),
]
