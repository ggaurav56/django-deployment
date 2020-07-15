from django.urls import path
from blog import views



urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/create',views.PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('post/<int:pk>/update',views.PostUpdateView.as_view(),name='post_update'),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name='post_delete'),
    path('post/<int:pk>/publish',views.post_publish,name='post_publish'),
    path('post/<int:pk>/comment',views.add_comments_post,name='add_comments_post'),
    path('comment/<int:pk>/delete',views.comment_delete,name='comment_delete'),

]
