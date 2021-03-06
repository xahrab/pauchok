import datetime
from django.urls import path
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Post, id= request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args = [str(pk)]))
    
 
class HomeView(ListView):
    model = Post
    template_name = 'home/index.html'
    ordering = ['post_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'home/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context



class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'home/add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body','author')

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    #fields = ['title','author','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'home/delete.html'
    success_url = reverse_lazy('home')