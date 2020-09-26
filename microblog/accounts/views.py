from django.shortcuts import render
from django.views import generic
from accounts import forms, models
from django.urls import reverse_lazy

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'accounts/home.html'


class CreateUserView(generic.CreateView):
    form_class = forms.UserForm
    template_name = 'accounts/user_createform.html'
    success_url = reverse_lazy('posts:home')

class CreateProfile(generic.CreateView):
    form_class = forms.UserProfileForm
    template_name = 'accounts/create_profile.html'
    success_url = reverse_lazy('posts:home')

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

