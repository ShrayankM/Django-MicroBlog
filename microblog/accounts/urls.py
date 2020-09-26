from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    # path('', views.HomeView.as_view(), name = 'home'),
    path('createuser/', views.CreateUserView.as_view(), name = 'createuser'),
    path('createprofile/', views.CreateProfile.as_view(), name = 'createprofile'),
    path('updateprofile/<int:pk>', views.UpdateProfile.as_view(), name = 'updateprofile'),
    path('profiledetail/<int:pk>', views.DetailProfile.as_view(), name = 'profiledetail'),
    path('loginuser/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name ='loginuser'),
    path('logoutuser/', auth_views.LogoutView.as_view(), name ='logoutuser'),
]