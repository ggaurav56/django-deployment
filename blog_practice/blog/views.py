from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Comment,Post
from blog.forms import CommentForm,PostForm
from django.views.generic import ListView,TemplateView,DetailView,UpdateView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy

# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView,LoginRequiredMixin):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

class PostDeleteView(DeleteView,LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post_list')

class PostCreateView(CreateView,LoginRequiredMixin):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

#####################################
#####################################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)


def add_comments_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)

    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_delete(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
