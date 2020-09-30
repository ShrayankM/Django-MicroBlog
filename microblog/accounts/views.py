from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from accounts import forms, models
from django.urls import reverse_lazy, reverse
from posts.models import Post as post_model 
from accounts.models import UserProfile as user_model
from django.utils import timezone

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'accounts/home.html'


class CreateUserView(generic.CreateView):
    form_class = forms.UserForm
    template_name = 'accounts/user_createform.html'
    success_url = reverse_lazy('accounts:loginuser')

class CreateProfile(generic.CreateView):
    form_class = forms.UserProfileForm
    template_name = 'accounts/create_profile.html'
    success_url = reverse_lazy('posts:home')

    def get(self, *args, **kwargs):
        try:
            if self.request.user.users:
                return HttpResponseRedirect(reverse("posts:home"))
        except ObjectDoesNotExist:
            return super().get(*args, **kwargs)
        return super().get(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user  = self.request.user
        return super().form_valid(form)

class UpdateProfile(generic.UpdateView):
    model = models.UserProfile
    form_class = forms.UserProfileForm
    template_name = 'accounts/update_profile.html'
    success_url = reverse_lazy('posts:home')


        
class DetailProfile(generic.DetailView):
    model = models.UserProfile
    template_name = 'accounts/profile_detail.html'

    def get_context_data(self, **kwargs):
        profile = get_object_or_404(models.UserProfile, id = self.kwargs['pk'])
        posts = post_model.objects.filter(author = profile.user, published_date__lte = timezone.now()).order_by("-published_date")
        drafts = post_model.objects.filter(author = profile.user, published_date__isnull = True).order_by("-created_date")
        context = super().get_context_data(**kwargs)
        context["posts"] = posts 
        context["drafts"] = drafts
        return context
    

