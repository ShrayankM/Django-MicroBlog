from django.shortcuts import render, get_object_or_404
from django.views import generic
from posts import models, forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class HomeView(generic.ListView):
    model = models.Post
    template_name = 'posts/home.html'
    context_object_name = 'postlist'
    
class CreatePost(generic.CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'posts/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(generic.UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'posts/update_post.html'


class PostDetail(generic.DetailView):
    model = models.Post
    template_name = 'posts/post_detail.html'


def post_like(request, pk):
    post = get_object_or_404(models.Post, id = pk)
    post.save()
    check = request.POST.get('check')
    if check == "1":
        post.likes.add(request.user);
        if post.dislikes.filter(id = request.user.id).exists():
            post.dislikes.remove(request.user)
    else: 
        post.dislikes.add(request.user)
        if post.likes.filter(id = request.user.id).exists():
            post.likes.remove(request.user)
    return HttpResponseRedirect(reverse('posts:postdetail', kwargs = {'pk' : pk}))



class CreateComment(generic.CreateView):
    model = models.Comment
    form_class = forms.CommentForm
    template_name = "posts/create_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

