from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse_lazy
from django.views import generic
from posts import models, forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.models import UserProfile
from django.utils import timezone

# Create your views here.
class HomeView(generic.ListView):
    model = models.Post
    template_name = 'posts/home.html'
    context_object_name = 'postlist'

    # def get_queryset(request):
    #     return models.Post.objects.filter(published_date__lte = timezone.now()).order_by("-published_date")

    
class CreatePost(generic.CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'posts/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeletePost(generic.DeleteView):
    model = models.Post
    template_name = "posts/delete_post.html"
    success_url = reverse_lazy("posts:home")

    
    def get_context_date(self, **kwargs):
        post = get_object_or_404(models.Post, id = kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context["post"] = post
        return context
   
    
    
    


class UpdatePost(generic.UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'posts/update_post.html'


class PostDetail(generic.DetailView):
    model = models.Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        post = get_object_or_404(models.Post, id = self.kwargs['pk'])
        comment_form = forms.CommentForm()
        profile = UserProfile.objects.get(user = post.author)
        context = super().get_context_data(**kwargs)
        context["userprofile"] = profile
        context["form"] = comment_form
        return context


class DraftDetail(generic.DetailView):
    model = models.Post
    template_name = 'posts/draft_detail.html'
    
    

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



# class CreateComment(generic.CreateView):
#     model = models.Comment
#     form_class = forms.CommentForm
#     template_name = "posts/create_comment.html"

#     def form_valid(self, form):
#         form.instance.post_id = self.kwargs['pk']
#         return super().form_valid(form)

def create_comment(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect("posts:postdetail", pk=post.pk)

def delete_post(request, pk):
    post = get_object_or_404(models.Post, pk = pk)
    post.delete()
    return redirect("posts:home")


def post_publish(request, pk):
    post = get_object_or_404(models.Post, pk = pk)
    post.publish()
    return redirect("posts:postdetail", pk = pk)

